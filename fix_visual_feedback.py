# -*- coding: utf-8 -*-
"""
Fix visual feedback from user screenshot:
1. Remove the giant solid white ring (cymascope_basin.glb)
2. Replace multi-point exciter with Single Central Gaussian Exciter (pure CymaScope r=0)
3. Frequency normalization so high frequencies (>1000 Hz) don't create sharp spikes
4. Smooth circular radial damping at perimeter
"""

with open('C:/Users/Pc/Downloads/Cimatic/index.html', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Remove the basin loading
basin_old = '''        // 1. Cubeta Metálica Física do CymaScope (Titânio Escovado)
        gltfLoader.load('assets/cymascope_basin.glb', (gltf) => {
          cymascopeBasinMesh = gltf.scene;
          cymascopeBasinMesh.position.set(0, 0, 0);
          scene.add(cymascopeBasinMesh);
          console.log("CymaScope Basin carregado com sucesso do Blender!");
        }, undefined, (err) => console.log("Basin fallback:", err));'''

basin_new = '''        // 1. Cubeta Metálica Física do CymaScope (Desativada para manter a lâmina limpa sem o aro branco)
        // A mesa já possui acabamento em espelho negro PBR limpo e minimalista.'''

if basin_old in code:
    code = code.replace(basin_old, basin_new, 1)
    print("Removed white basin ring from scene.")

# 2. Update fluid solver code
fluid_old = '''      // --- SOLVER DE ÁGUA FÍSICA MESOTÓPICA (CIMATICAGUAFLUIDA.HTML) ---
      const fluidVisc = STUDIO_STATE.viscosity || 0.985;
      const fluidStab = audioState.stability || 0.8;
      const ds = fluidVisc - (fluidStab * 0.005);
      const ws = 0.12 + (fluidStab * 0.04);

      // Excitação por som real (oscilador ou microfone/arquivo)
      let fluidVol = 0;
      if (AudioEngine.isOscillatorActive) {
        fluidVol = 0.32 * (STUDIO_STATE.gain / 35.0);
      } else if (AudioEngine.currentSourceType !== null && audioState.volume > 0.001) {
        fluidVol = Math.min(1.0, audioState.volume * 2.5) * (STUDIO_STATE.gain / 35.0);
      }

      if (fluidVol > 0.0005) {
        const bp = elapsedTime * activeHz * 0.01;
        fluidExciters.forEach(ex => {
          const idx = Math.floor(ex.y * gFluidRes) * gFluidRes + Math.floor(ex.x * gFluidRes);
          hField[idx] += Math.sin(bp + ex.phase) * fluidVol * ex.weight;
        });
      }

      // Equação de onda de 2ª ordem em malha 2D (Laplaciano discreto isotrópico de 4 pontos)
      for (let y = 1; y < gFluidRes - 1; y++) {
        const row = y * gFluidRes;
        for (let x = 1; x < gFluidRes - 1; x++) {
          const i = row + x;
          vField[i] = (vField[i] + ((hField[i - 1] + hField[i + 1] + hField[i - gFluidRes] + hField[i + gFluidRes]) * 0.25 - hField[i]) * ws) * ds;
        }
      }
      for (let i = 0; i < totalFluid; i++) {
        hField[i] += vField[i];
      }'''

fluid_new = '''      // --- SOLVER DE ÁGUA FÍSICA MESOTÓPICA (CYMASCOPE PONTO CENTRAL ÚNICO) ---
      const fluidVisc = STUDIO_STATE.viscosity || 0.985;
      const fluidStab = audioState.stability || 0.8;
      const ds = fluidVisc - (fluidStab * 0.005);
      const ws = 0.12 + (fluidStab * 0.04);

      // Excitação por som real (oscilador ou microfone/arquivo)
      let fluidVol = 0;
      if (AudioEngine.isOscillatorActive) {
        fluidVol = 0.25 * (STUDIO_STATE.gain / 35.0);
      } else if (AudioEngine.currentSourceType !== null && audioState.volume > 0.001) {
        fluidVol = Math.min(1.0, audioState.volume * 2.0) * (STUDIO_STATE.gain / 35.0);
      }

      // Normalização física para altas frequências (evita agulhas e vincos acima de 1000 Hz)
      const freqScale = Math.min(1.0, Math.sqrt(350.0 / Math.max(100.0, activeHz)));
      fluidVol *= freqScale;

      if (fluidVol > 0.0005) {
        const bp = elapsedTime * activeHz * 0.01;
        // Ponto Focal Central Único com dispersão gaussiana suave de raio 2 células
        const cx = Math.floor(gFluidRes / 2);
        const cy = Math.floor(gFluidRes / 2);
        for (let dy = -2; dy <= 2; dy++) {
          for (let dx = -2; dx <= 2; dx++) {
            const d2 = dx * dx + dy * dy;
            if (d2 <= 5) {
              const weight = Math.exp(-d2 / 2.2);
              const idx = (cy + dy) * gFluidRes + (cx + dx);
              hField[idx] += Math.sin(bp) * fluidVol * weight * 0.38;
            }
          }
        }
      }

      // Equação de onda de 2ª ordem em malha 2D (Laplaciano discreto isotrópico) com PML radial
      for (let y = 1; y < gFluidRes - 1; y++) {
        const row = y * gFluidRes;
        const normY = (y / gFluidRes) * 2 - 1;
        for (let x = 1; x < gFluidRes - 1; x++) {
          const i = row + x;
          const normX = (x / gFluidRes) * 2 - 1;
          const rNorm = Math.sqrt(normX * normX + normY * normY);

          // Amortecimento gradual na borda radial
          let edgeDamp = ds;
          if (rNorm > 0.85) {
            const pml = (rNorm - 0.85) / 0.15;
            edgeDamp *= Math.max(0.70, 1.0 - pml * 0.25);
          }

          vField[i] = (vField[i] + ((hField[i - 1] + hField[i + 1] + hField[i - gFluidRes] + hField[i + gFluidRes]) * 0.25 - hField[i]) * ws) * edgeDamp;
        }
      }
      for (let i = 0; i < totalFluid; i++) {
        hField[i] += vField[i];
      }'''

if fluid_old in code:
    code = code.replace(fluid_old, fluid_new, 1)
    print("Replaced fluid solver with single central exciter and radial damping.")

# Also in Mesa 1 vertex displacement, smooth circular boundary:
water_disp_old = '''        if (STUDIO_STATE.activeMesa === 'water_pure') {
          // ========================================================
          // MESA 1: ÁGUA FÍSICA MESOTÓPICA (CIMATICAGUAFLUIDA.HTML)
          // ========================================================
          // Altura calculada pelo solver físico de malha 2D (hField)
          const fluidDisp = hField[i] * (12.0 + fluidStab * 18.0) * (STUDIO_STATE.gain / 35.0);'''

water_disp_new = '''        if (STUDIO_STATE.activeMesa === 'water_pure') {
          // ========================================================
          // MESA 1: ÁGUA FÍSICA MESOTÓPICA (CYMASCOPE - PONTO CENTRAL)
          // ========================================================
          // Altura calculada pelo solver físico de malha 2D (hField)
          let fluidDisp = hField[i] * (12.0 + fluidStab * 18.0) * (STUDIO_STATE.gain / 35.0);

          // Suavização nas bordas circulares da cubeta
          const R_cuv = 8.8;
          if (r > R_cuv) {
            fluidDisp *= Math.max(0, 1.0 - (r - R_cuv) / 0.5);
          }'''

if water_disp_old in code:
    code = code.replace(water_disp_old, water_disp_new, 1)
    print("Added circular edge smoothing to water_pure.")

with open('C:/Users/Pc/Downloads/Cimatic/index.html', 'w', encoding='utf-8') as f:
    f.write(code)

print("SUCCESS: index.html fully refined!")
