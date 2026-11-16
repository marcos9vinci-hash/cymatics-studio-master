# Cymatics Studio Master 🌊✨

Laboratório virtual multifísico de simulação e visualização cimática 3D em tempo real, construído com **Three.js (WebGL / GLSL)** e **Web Audio API**.

Inspirado nas pesquisas pioneiras de Ernst Chladni, Hans Jenny, Alexander Lauterwasser e no CymaScope Pro de John Stuart Reid.

---

## 🚀 Funcionalidades Principais

1. **Mesa 1 — Água Pura (CymaScope / Ondas de Faraday):**
   - Excitação por **ponto focal central único** ($r = 0$) com reflexão coerente de borda.
   - Instabilidade sub-harmônica de Faraday ($f_0/2$) com termos não-lineares ($c_2, c_3$).
   - Fluido raso calibrado ($
u = 5.50 \times 10^{-5}\text{ m}^2/\text{s}$, $H = 1.50\text{ mm}$, $\sigma = 0.0450\text{ N/m}$, $\rho = 1120\text{ kg/m}^3$) com retorno instantâneo (< 16 ms) ao espelho plano no silêncio.

2. **Mesa 2 — Placa de Chladni (Dinâmica Granular de Areia):**
   - 25.000 microgrãos de quartzo dourados (`THREE.Points`).
   - Força acústica de deriva $\mathbf{F}_{\text{ac}} = -2\alpha |u| \nabla |u|$ empurrando os grãos para fora dos antinodos.
   - **Travamento Estático Estrito**: Quando $\Gamma < 1.0$ ou na linha nodal ($|u| < 0.018$), a probabilidade de salto é zero ($P_{\text{hop}} = 0$) e a velocidade é rigidamente anulada, congelando os grãos imóveis sobre as linhas nodais sem trepidação artificial.

3. **Mesa 3 — Fusão Cimática Híbrida (Acoplamento Nodal na Água):**
   - Máscara nodal gaussiana $S(x, z, t) = A_{\text{drive}}(t) \cos(\omega t) \exp(-|u|^2 / \varepsilon^2)$ onde a figura de Chladni atua como matriz de micro-alto-falantes submersos excitando a água.
   - Camada esponja absorvente PML radial ($r > 0.85 R$) dissipando energia antes da borda.
   - Persistência temporal de onda (`persistenceFactor`).

4. **Óptica PBR "Espelho Negro":**
   - `emissiveIntensity = 0.0` no acabamento espelho negro, com contraste 100% óptico por inclinação de superfície ($
abla h$) e curvatura ($
abla^2 h$).
   - Anel de LEDs rasante (75°–85°) e luzes 3D arrastáveis com gizmos.
   - 33 raios geométricos com 12 coreografias algorítmicas (*Pulsar*, *Girar*, *8 Loop*, *Vortex*, *Salto*, *Arco-Íris*, *Hz Color*, *Caleidoscópio*, *Flash Reto*, *Espiral*, *Inverter*, *Cores*).

5. **Motor de Áudio & Atlas Hz:**
   - Três fontes: Microfone ao vivo, Upload de faixas e Oscilador Senoidal Interno suave.
   - Análise FFT + detector de pitch por autocorrelação e detector $dE/dt$ de batida.
   - Atlas completo de 25 presets científicos (20 Hz a 2000 Hz + série harmônica Solfeggio).
   - 6 Nós de Viscosidade Anuhazi (.940 a .985).
   - AI Visual DJ com 4.000 partículas em `AdditiveBlending`.

---

## 🛠️ Como Executar

Basta abrir o arquivo `index.html` em qualquer navegador moderno com suporte a WebGL e Web Audio API, ou iniciar um servidor local:

```bash
# Servidor local simples
python -m http.server 8080
```
Depois acesse `http://localhost:8080` no navegador.
