# RESUMO EXECUTIVO & DOSSIÊ SINTÉTICO: CYMATICS STUDIO MASTER

**Projeto:** Cymatics Studio Master (Simulador Multifísico 3D de Cimática em Tempo Real)  
**Tecnologias:** Three.js (WebGL / GLSL), Web Audio API, Tailwind CSS, JavaScript Modular Vanilla  
**Status de Execução:** Fases A, B e C 100% Concluídas e Auditadas em Navegador Real  

---

## 1. Visão Geral do Sistema
O **Cymatics Studio Master** é uma estação digital profissional de simulação multifísica e visualização cimática 3D em tempo real. Inspirado nos aparatos científicos de Hans Jenny, Alexander Lauterwasser e no CymaScope Pro de John Stuart Reid, o sistema traduz frequências sonoras puras, microfone ao vivo e faixas de áudio em relevos tridimensionais hidro-acústicos e padrões granulares de interferência nodal com rigor físico e óptico.

---

## 2. As Três Mesas Cimáticas Fundamentais

### Mesa 1: Água Pura (CymaScope)
* **Princípio Físico:** Excitação por **ponto focal central único** ($r = 0$). Ondas cilíndricas de Bessel/Hankel irradiam radialmente para fora, atingem a borda circular rígida da cubeta ($R = 8.8$) e refletem coerentemente de volta para o centro, gerando ondas estacionárias axissimétricas.
* **Instabilidade de Faraday Sub-Harmônica:** Resposta na frequência $f_0/2$ governada pela equação de Mathieu amortecida. Inclui termos não-lineares quadráticos ($c_2 = 0.25$) e cúbicos ($c_3 = 0.12$) para estabilizar redes quadradas e poligonais puras sem colapso em listras.
* **Fluido Raso Calibrado:** Parametrizado com viscosidade cinemática $\nu = 5.50 \times 10^{-5}\text{ m}^2/\text{s}$, lâmina líquida $H = 1.50\text{ mm}$, tensão superficial $\sigma = 0.0450\text{ N/m}$ e densidade $\rho = 1120\text{ kg/m}^3$.
* **Silêncio Imediato:** O alto atrito de fundo da lâmina rasa garante tempo de decaimento $\tau < 16\text{ ms}$, retornando instantaneamente a superfície ao repouso espelhado plano no silêncio (sem persistência residual).

### Mesa 2: Placa de Chladni (Dinâmica Granular de Areia)
* **Princípio Físico:** Chapa quadrada de bordas livres de $18 \times 18$ excitada modalmente por superposição degenerada de autofunções de Kirchhoff:
  $$u(x, z) = a \cos\left(\frac{n\pi x}{L}\right)\cos\left(\frac{m\pi z}{L}\right) + b \cos\left(\frac{m\pi x}{L}\right)\cos\left(\frac{n\pi z}{L}\right)$$
* **25.000 Microgrãos de Quartzo:** Partículas físicas renderizadas via `THREE.Points` com variação de cor dourada/bege.
* **Deriva Acústica e Difusão de Itô:** A força de radiação acústica $\mathbf{F}_{\text{ac}} = -2\alpha |u| \nabla |u|$ empurra os grãos para fora dos antinodos em direção às linhas nodais ($u = 0$).
* **Travamento Estático Estrito (Anti-Jitter):** Quando a aceleração adimensional cai abaixo da gravidade ($\Gamma = \frac{|u|\omega^2}{g} < 1.0$) ou o grão atinge a vizinhança nodal ($|u| < 0.018$), a probabilidade de salto $P_{\text{hop}} = 0$ e a velocidade é rigidamente anulada por atrito estático. Os grãos congelam completamente imóveis sobre a figura geométrica.

### Mesa 3: Fusão Cimática Híbrida (Próxima Fase)
* **Acoplamento Nodal-Fluídico:** A figura nodal de Chladni atua como uma matriz contínua de micro-excitadores submersos injetando energia na equação de onda da água (EDP de 4ª ordem capilar-gravitacional com camada esponja absorvente PML).

---

## 3. Óptica PBR "Espelho Negro" & Iluminação Rasante

* **Zero Emissão Lavada:** No acabamento *Espelho Negro*, a intensidade emissiva é estritamente zero (`emissiveIntensity = 0.0`). O contraste óptico de 100% nasce exclusivamente da inclinação geométrica da superfície ($\nabla h$) refletindo a luz rasante.
* **Normais por Diferenças Centrais:** Normais de superfície calculadas a cada quadro em tempo real:
  $$\mathbf{N} = \text{normalize}(h_L - h_R, 2\Delta x, h_D - h_U)$$
* **Fresnel de Schlick & GGX:** Rugosidade ultrabaixa ($\alpha = 0.035$) com refletância normal $F_0 = 0.02 - 0.04$ (água dielétrica profunda) ou $F_0 = 0.56 - 0.72$ (mercúrio negro).
* **Anel Rasante de LEDs (75°–85°):** Anel de 16 LEDs em ângulo rasante ($H_{\text{ring}} / D_{\text{ring}} \approx 0.25$) para que o centro plano permaneça escuro e apenas as cristas e vales inclinados brilhem.
* **Luzes Customizadas 3D Arrastáveis:** Luzes pontuais com gizmos interativos arrastáveis via Raycaster em plano horizontal, com alcance e atenuação calibrados para evitar saturação branca central (*washout*).
* **Sistema de 33 Raios Geométricos:** Até 33 feixes de luz radiais com 12 coreografias algorítmicas (*Pulsar*, *Girar*, *8 Loop / Lissajous*, *Vortex*, *Salto / Beat Sync*, *Arco-Íris*, *Hz Color*, *Caleidoscópio*, *Flash Reto*, *Espiral Hipno*, *Inverter* e *Cores*).

---

## 4. Motor Acústico (Web Audio API) & Atlas Hz

* **Três Entradas de Sinal:** Microfone ao vivo (baixa latência), Upload de arquivos de áudio e Oscilador Senoidal Interno de precisão (com rampas de ganho suaves sem estalos).
* **Telemetria Dupla:** Leitura FFT de frequência dominante acoplada a detector de Pitch por Autocorrelação temporal.
* **Detector de Batida ($dE/dt$):** Monitoramento contínuo da derivada de energia espectral acionando LED pulsante de *Beat Sync* e sincronismo visual.
* **Medidor de Estabilidade Harmônica:** Avaliação percentual contínua de coerência harmônica do sinal sonoro.
* **Atlas de 25 Presets Científicos Calibrados:** Catálogo completo integrado dos 20 Hz aos 2.000 Hz, cobrindo o espectro grave (ondas gravitacionais), médio (figuras florais e poligonais) e agudo (retículas capilares), incluindo a série harmônica Solfeggio (174 Hz, 396 Hz, 432 Hz, 528 Hz, etc.).

---

## 5. Interface & Ergonomia de Controle
* **Barra Superior Compacta:** Seletor direto das 3 Mesas, 4 Assinaturas Clássicas visuais, alternador de Câmera 3D / Zenital (com interpolação suave lerp) e acionamento de Modo Sessão Imersiva.
* **Sidebar Única em 5 Camadas (Acordeão Auto-Recolhível):**
  1. *Áudio & Mixer* (fontes, ganho, filtro LowPass 50–2000 Hz, detectores)
  2. *Física da Mesa* (ganho de excitação, viscosidade, dispersão de areia Chladni, modos harmônicos)
  3. *Luzes & Óptica* (acabamentos, anel rasante, luzes arrastáveis, 33 raios e coreografias)
  4. *Atlas Hz* (oscilador senoidal, catálogo de presets filtrável por faixas)
  5. *VJ & Sessão* (AI Visual DJ, temporizador de meditação/imersão)
