### Plano Mestre de Engenharia e Arquitetura (5 Etapas) para Build 3D no Argon: Cymatics Studio Master

O desenvolvimento de um laboratório cimático interativo em Three.js, WebGL/GLSL e Web Audio API tende a falhar quando a geração de código parte diretamente de um pedido amplo e monolítico. A evolução documentada nos oito protótipos anteriores do projeto  *Cymatics Lab*  demonstra que tentativas de unificar funcionalidades sem congelar primeiro a arquitetura física e de interface produzem regressões previsíveis: iluminação emissiva que apaga o relevo 3D e confere à superfície uma aparência plana de 2D, soma excessiva de luzes pontuais que estoura o centro em branco, dinâmica líquida com latência elevada incapaz de acompanhar voz ou batidas musicais, múltiplos excitadores fixos que destroem a simetria radial central e controles espalhados por toda a tela. A sequência estruturada em cinco etapas descrita neste documento estabelece a ordem rigorosa de engenharia necessária para consolidar o  *Cymatics Studio Master*  antes e durante a execução modular nos ambientes Argon e Hydrogen.

#### 1\. Visão Geral da Sequência Obrigatória de 5 Etapas Antes do Build Final

Organizar a construção em cinco estágios sequenciais garante que nenhuma camada visual, sonora ou de interface seja codificada antes de seu modelo físico e seu contrato de dados estarem fechados. Conforme a Auditoria Técnica Completa dos oito códigos HTML predecessores e a síntese computacional de modelagem multifísica do projeto, cada etapa atua como uma barreira de verificação contra inconsistências numéricas e visuais antes de enviar especificações ao gerador de código.  
Etapa,Artefato / Ação de Engenharia,Objetivo Estrutural no Projeto,Base Documental e Fontes,Critério de Saída (Gate) e Estado Atual  
Etapa 1,Mapa Mental de Arquitetura e Congelamento de Escopo,Reduzir o excesso de mesas experimentais para exatamente 3 Mesas de Simulação e definir a Sidebar única em camadas com modais contextuais.,Auditoria Técnica dos 8 Aplicativos; especificação arquitetural de 3 mesas e interface em camadas.,Escopo congelado sem botões dispersos ou modos redundantes ( Concluída  no Mapa Mental do painel Studio).  
Etapa 2,"Auditoria Cirúrgica de Código (""O que Fica vs. O que Sai"")",Mapear módulo a módulo os ganhos dos 8 códigos anteriores (cimatic.html a cimaticaguafluida.html) e diagnosticar os gargalos 2D e de latência da última revisão.,Auditoria Técnica Completa dos 8 Códigos; código-fonte da última revisão HTML.,"Lista fechada de parâmetros preservados, corrigidos e descartados ( Parcial : 8 protótipos auditados; código bruto da revisão mais recente pendente de inspeção direta)."  
Etapa 3,Fonte Única de Dados: Atlas de Frequências e Presets JSON,Eliminar multiplicadores trigonométricos arbitrários por meio de um catálogo calibrado de 20 Hz a 2000 Hz e série Solfeggio.,Val Baker et al. (2024); Sheldrake & Sheldrake (2017); Geffen et al. (2025); Shao et al. (2021); Dossiê Técnico.,"Esquema JSON padronizado validado com modos  \$(m,n)\$ , pesos  \$(a,b)\$ , simetria e amortecimento ( Concluída  no Dossiê Técnico)."  
Etapa 4,Contrato Multifísico 3D e Shaders GLSL,"Especificar as equações de Kirchhoff–Love, travamento granular ( \$\\Gamma \< 1\$ ), fluido raso rápido, EDP híbrida CFL/PML e óptica PBR de Espelho Negro.",Tuan et al. (2015); Devauchelle et al. (2026); Phenomena Study \#29; LearnOpenGL; T. Ramaswamy; Modelagem Computacional 3D.,"Uniforms, estênceis discretos, condição CFL e  fragment shader  PBR especificados ( Concluída  no Dossiê Técnico e consolidada na Seção 5)."  
Etapa 5,Blueprint Modular e Prompts em Fases para Argon / Hydrogen,Dividir a implementação em 4 fases testáveis (UI → Áudio/Dados → Mesas 1 e 2/PBR → Mesa 3 Híbrida/DJ) com critérios objetivos de aceite.,Consolidação das Etapas 1 a 4.,Pacote de prompts faseados pronto para execução sequencial no Argon e Hydrogen ( Entregue na Seção 6 ).  
A passagem ordenada por essas cinco etapas impede que a geração de código misture equações trigonométricas planas com  *solvers*  de campo de altura, preservando a separação limpa entre interface, catálogo de frequências, física de GPU e renderização óptica.

#### 2\. Etapa 1 — Congelamento de Escopo: As 3 Mesas, Sidebar em Camadas e Assinaturas Clássicas

A proliferação de variantes experimentais nos protótipos iniciais diluía o foco do laboratório virtual. O congelamento de escopo estabelece uma arquitetura enxuta centrada em exatamente três mesas de simulação física e em uma interface hierarquizada em camadas, evitando conflitos conceituais entre meios sólidos e líquidos.

##### 2.1 Redução Estrutural para Exatamente 3 Mesas de Simulação

Cada mesa representa um domínio físico distinto, corrigindo erros anteriores como renderizar grãos sólidos como se fossem fluido ou distribuir múltiplos pontos focais onde a física do CymaScope exige excitação central única.

1. **Mesa 1 — Água Pura (Estilo CymaScope / Ondas de Faraday):**  Bacia circular ou quadrada com acabamento de Espelho Negro, excitada por um  **único ponto focal central**  (pistão ou bobina de voz). As ondas partem do centro, refletem na borda e formam ondas estacionárias sub-harmônicas ( \$f\_0/2\$ ) com resposta instantânea à voz humana e à música, retornando imediatamente ao espelho plano durante o silêncio.  
2. **Mesa 2 — Placa de Chladni (Microgrãos de Areia):**  Chapa metálica rígida vibrante na qual milhares de microgrãos saltam das regiões de alta amplitude (ventres ou antinodos) e migram para as linhas de repouso absoluto (linhas nodais  \$u \= 0\$ ), estabilizando-se sem trepidação artificial após a formação da figura geométrica.  
3. **Mesa 3 — Fusão Cimática Híbrida (Geometria na Água):**  Acoplamento direto entre os dois domínios físicos, no qual a condição nodal formada pela Placa de Chladni ( \$\|u(x,z)\| \< \\varepsilon\$ ) atua como uma matriz distribuída de micro-alto-falantes sob a lâmina d'água, fazendo com que a própria forma geométrica nodal (cruz, estrela, flor, hexágono ou mandala) vibre e emita micro-ondas concêntricas sobre a superfície líquida.

##### 2.2 Arquitetura de UI/UX em Sidebar por Camadas e Perfis Rápidos

Para eliminar botões dispersos no topo, nas laterais e na base da tela — além de painéis verticais longos que obstruem a visualização 3D —, a interface adota uma  **Sidebar única organizada por camadas** . Uma barra superior enxuta concentra apenas o seletor das 3 Mesas, os 4 botões de  **Assinatura Clássica de 1 Clique**  recomendados na Auditoria Técnica dos 8 Aplicativos e o acionador do  **Modo Sessão** . Na lateral, uma coluna compacta exibe cinco botões de camada:  **Áudio & Mixer** ,  **Física da Mesa** ,  **Luzes & Óptica** ,  **Atlas de Frequências (Hz)**  e  **VJ / Sessão** . Acionar qualquer camada abre exclusivamente o modal contextual correspondente ancorado dentro da própria sidebar, recolhendo os demais automaticamente para manter o palco 3D livre.  
Os quatro perfis de  **Assinatura Clássica**  permitem alternar instantaneamente toda a calibração da cena entre os pontos altos dos protótipos históricos:  **Cimatic 3 (Visual Perfeito)**  para espelho negro puro sem emissão artificial (emissiveIntensity: 0),  **Cimatic 4 (Mesa Top Luz Suave)**  para atenuação calibrada de raios sem estouro branco no centro,  **Cimatic 6 (VJ DJ Immersion)**  para resposta rítmica por picos de energia (energyPeak) e 33 raios coreografados, e  **Água Fluida (Anuhazi Mesotopic)**  para simulação hidrodinâmica em campo de altura com presets harmônicos e controle de viscosidade. Com o escopo das mesas e da interface congelado, a etapa seguinte audita o código legado para definir exatamente quais mecanismos técnicos migram para o motor 3D definitivo.

#### 3\. Etapa 2 — Auditoria Cirúrgica dos 8 Códigos e Diagnóstico do Salto 2D para 3D

A comparação linha a linha realizada na Auditoria Técnica Completa dos oito arquivos HTML (cimatic.html, cimatic2.html, cimatic3visualperfeito.html, cimatic4mesatopluzfraca.html, cimatic5.html, cimatic6dj.html, cimaticlabsanuhazi.html e cimaticaguafluida.html) mostra que cada versão resolveu um problema de engenharia específico enquanto deixava para trás avanços de versões irmãs. Dar o salto definitivo de um visual plano para uma simulação 3D de alto contraste exige preservar seletivamente os componentes vencedores e corrigir quatro gargalos estruturais.

##### 3.1 Matriz "O que Fica vs. O que Sai" dos Oito Protótipos

A tabela a seguir consolida os parâmetros e soluções de código validados em cada geração e define o destino arquitetural de cada módulo no  *Cymatics Studio Master* .  
Protótipo de Origem,Mecanismos e Parâmetros Validados (O que Fica),Limitações Diagnosticadas (O que Sai / É Corrigido),Papel na Arquitetura 3D Final  
cimatic.html  e  cimatic2.html,Malha base PlaneGeometry  \$18\\times 18\$  com resolução  \$160\\times 160\$ ; luzes customizadas arrastáveis no plano 3D via Raycaster; distribuição radial rayLights em  \$2\\pi/\\text{count}\$ .,"Estouro de brilho branco no centro da placa quando muitos raios eram ativados simultaneamente, escondendo o relevo 3D.",Base geométrica de arraste Raycaster expandida com controles explícitos para altura  \$Y\$  e ângulo.  
cimatic3visualperfeito.html,"Material enxuto (arquivo de  \$26{,}3\\text{ KB}\$ ) sem emissão artificial (emissiveIntensity: 0), color: 0x08080c, metalness: 0.96 e roughness: 0.14.",Ausência de seletor para alternar modos de superfície em contextos terapêuticos ou de VJ.,Modo padrão  Espelho Negro (Visual Perfeito)  na Mesa 1 e opção principal no seletor de acabamento.  
cimatic4mesatopluzfraca.html,"Atenuação calibrada de distance nas PointLight e altura reduzida dos raios (yPos \= 1.4); equação Math.cos(f \* x) \* Math.cos(f \* z) \* Math.sin(f \* r \- time) com amortecimento radial; modos  Caleidoscópio Original ,  Flash Reto ,  Espiral Hipno  e  Inverter .",Formulação trigonométrica analítica rígida para simular propagação hidrodinâmica real em fronteiras arbitrárias.,Calibragem padrão de alcance luminoso e foco/suavidade dos raios sem lavar o centro de branco.  
cimatic5.html  e  cimatic6dj.html,"Limite expandido para 33 raios radiais com seletores individuais de cor; coreografias ( 8 Loop ,  Vortex  ascendente em Y,  Salto  na batida grave,  Arco-Íris ,  Hz Color ); 4 modulações físicas ( Ressonância ,  Fluido/Mercúrio  com deslocamento X/Z dos vértices,  Excitação Multi-Ponto ,  Overdrive Chladni );  \$4.000\$  partículas flutuantes em AdditiveBlending; AI Visual DJ por energyPeak e Filtro LowPass em tempo real.","Troca aleatória por tempo no AI DJ inicial (corrigida no 6dj); ausência de slider contínuo de corte LowPass ( \$50\\text{ Hz}\$  a  \$2000\\text{ Hz}\$ ), Volume Master e LED de batida na versão unificada.","Camada completa de Mixer DJ, modulação física 3D (deslocamento X/Z de mercúrio), AI DJ por pico e partículas reativas."  
cimaticlabsanuhazi.html,Interface glass-ui em vidro escuro com tipografia dourada/violeta; 9 presets Solfeggio ( \$174\\text{ Hz}\$  a  \$852\\text{ Hz}\$ ) com oscilador senoidal interno ( fade-in/fade-out  sem estalos); medidor de estabilidade  Harmonic Resonance ; 6 nós de cor alterando viscosidade (0.940 Rubi a 0.985 Violeta); Modo Sessão com cronômetro e bloqueio de cliques acidentais.,"Brilho emissivo mesotópico ativo continuamente, ofuscando o reflexo puro quando aplicado à água de espelho negro.","Gerador harmônico interno, medidor de estabilidade e Modo Sessão; emissão movida para opção selecionável ( Anuhazi Emissivo )."  
cimaticaguafluida.html,Simulação real de Equação de Onda 2D em tempo real usando matrizes hField (altura) e vField (velocidade vertical) com  \$161\\times 161\$  células; botão  Estabilização Cimática  com persistenceFactor.,Cinco excitadores fixos simultâneos (indesejados na Mesa 1 centralizada) e resposta lenta sem acoplamento dinâmico às luzes arrastáveis.,"Motor evoluído para GPU (RGBA32F) com 1 foco central na Mesa 1, máscara nodal na Mesa 3 e opção multi-ponto opcional."

##### 3.2 Diagnóstico dos Quatro Gargalos que Mantêm a Simulação com Aspecto "2D"

A aparência achatada ou pouco tridimensional observada quando os módulos são combinados sem critérios decorre diretamente de quatro gargalos de renderização e física identificados na auditoria e nos estudos ópticos do projeto:

* **Lavagem Emissiva Global:**  Conforme diagnosticado na Auditoria Técnica dos 8 Códigos, manter o cálculo mesotópico (lightInertia somado a emissive) ativo sobre toda a placa mantém a superfície uniformemente acesa e destrói o contraste de sombras profundas do cimatic3visualperfeito.html, apagando a percepção de altura das cristas.  
* **Ausência de Normais Dinâmicas (**  **\$\\nabla h**\$  **) e Foco de Curvatura (**  **\$\\nabla^2 h**\$  **):**  Uma superfície deslocada apenas por senoides simples e sombreada de forma difusa não se comporta como espelho líquido. Nos experimentos com o CymaScope de Geffen et al. (2025) e na modelagem do  *Phenomena Study \#29* , o relevo 3D emerge porque a imagem capturada resulta diretamente da  **inclinação local**  da onda ( \$\\nabla h\$ ) refletindo fontes luminosas pontuais ou anelares sobre um fundo preto, com contraste amplificado pela curvatura superficial ( \$\\nabla^2 h\$ ).  
* **Iluminação Frontal em Vez de Incidência Rasante Calibrada:**  Luzes posicionadas próximas à normal vertical da câmera iluminam áreas planas em repouso e reduzem o contraste. A fotografia cimática profissional exige incidência lateral/rasante entre  \$75^\\circ\$  e  \$85^\\circ\$  em relação à normal plana, garantindo que o repouso permaneça negro e apenas as paredes inclinadas das ondas direcionem luz especular à câmera.  
* **Latência Hidrodinâmica por Amortecimento Macroscópico:**  Água comum apresenta decaimento viscoso lento ( \$12{,}5\\text{ s}\$  em  \$100\\text{ Hz}\$  e cerca de  \$50\\text{ s}\$  em baixos números de onda  \$k \= 100\\text{ m}^{-1}\$ ), mantendo ondas antigas na tela após o som parar e impedindo o acompanhamento preciso da voz humana ou de batidas percussivas rápidas.

##### 3.3 Protocolo de Inspeção Obrigatória da Última Revisão HTML Antes da Etapa 5

Como os arquivos text/html da pasta do Google Drive tiveram apenas metadados indexados e o código-fonte bruto da última revisão entregue fora da auditoria ainda não foi importado para inspeção direta no repositório, a Etapa 2 impõe um roteiro objetivo de verificação sobre esse arquivo antes do envio final ao Argon: checar se o material da placa força emissiveIntensity \> 0, verificar se o  *solver*  hField/vField roda em CPU ( \$161\\times 161\$ ) ou já utiliza  *framebuffers*  em GPU, confirmar se há múltiplos excitadores fixos ativos na Mesa 1 e validar se as partículas de Chladni possuem critério explícito de parada quando  \$\\Gamma \< 1{,}0\$ . Concluída a triagem técnica do legado, o próximo passo é travar os dados de frequência e geometria em um catálogo único.

#### 4\. Etapa 3 — Fonte Única de Dados: Atlas de Frequências, Modos (m, n) e Esquema JSON

Para impedir que o código gráfico gere padrões arbitrários desconectados da frequência sonora, o aplicativo deve consumir um catálogo centralizado como fonte única da verdade. A literatura experimental reunida no caderno estabelece distinções físicas fundamentais entre placas sólidas e fluidos: em placas elásticas finas, a dispersão flexural obedece a  \$k \= (\\rho h \\omega^2 / D)^{1/4}\$  e as ressonâncias seguem a Lei de Chladni  \$f \\approx C(m \+ 2n)^p\$  com  \$p \\approx 2\$  para chapas planas; já na água do CymaScope, a superfície responde na primeira sub-harmônica ( \$f\_0/2\$ ) sob a relação de dispersão gravidade-capilaridade  \$\\omega\_f^2 \= (gk \+ \\frac{\\sigma}{\\rho}k^3)\\tanh(kH)\$ .

##### 4.1 Âncoras Empíricas da Literatura e Mapeamento Áudio-Visual

As fontes primárias oferecem âncoras experimentais verificadas ao longo do espectro de  \$12\\text{ Hz}\$  a  \$2000\\text{ Hz}\$ . Em placas sólidas de Chladni, Val Baker et al. (2024) mapearam picos de impedância e contornos nodais em chapas de  \$24\\text{ cm}\$  para geometrias quadradas ( \$107\\text{ Hz}\$ ,  \$283\\text{ Hz}\$ ,  \$511\\text{ Hz}\$ ,  \$744\\text{ Hz}\$  e  \$1181\\text{ Hz}\$ ), circulares ( \$158\\text{ Hz}\$ ,  \$582\\text{ Hz}\$  e  \$1378\\text{ Hz}\$ ), triangulares ( \$152\\text{ Hz}\$ ) e hexagonais ( \$174\\text{ Hz}\$  em  \$12\\text{ cm}\$  e  \$9\\text{ cm}\$ , além de modos superiores até  \$1635\\text{ Hz}\$ ). No domínio líquido, Sheldrake e Sheldrake (2017) e Geffen et al. (2025) documentaram simetrias discretas  *n-fold*  no CymaScope Pro MF+ entre  \$12\\text{ Hz}\$  e  \$238\\text{ Hz}\$  (incluindo  \$26{,}5\\text{ Hz}\$ ,  \$35{,}34\\text{ Hz}\$ ,  \$36\\text{ Hz}\$ ,  \$43\\text{ Hz}\$ ,  \$45\\text{ Hz}\$ ,  \$56\\text{ Hz}\$ ,  \$66\\text{ Hz}\$ ,  \$69\\text{ Hz}\$ ,  \$73\\text{ Hz}\$ ,  \$78\\text{ Hz}\$ ,  \$82\\text{ Hz}\$ ,  \$89\\text{ Hz}\$ ,  \$111\\text{ Hz}\$ ,  \$129\\text{ Hz}\$ ,  \$180\\text{ Hz}\$  e  \$238\\text{ Hz}\$ ), o  *Phenomena Study \#29*  calibrou a rede quadrada sub-harmônica em  \$27\\text{ Hz}\$  (resposta a  \$13{,}5\\text{ Hz}\$  em células de  \$17\\text{ mm}\$ ) e a modelagem cilíndrica baseada em Shao et al. (2021) estendeu as ordens azimutais capilares para  \$500\\text{ Hz}\$   \$(18,6)\$ ,  \$1200\\text{ Hz}\$   \$(32,12)\$  e  \$2000\\text{ Hz}\$   \$(48,20)\$ .  
Adicionalmente, dois achados experimentais orientam diretamente o comportamento musical do motor: Zhou et al. (2016) demonstraram que placas acionadas no centro geram curvas nodais bem definidas em qualquer nota contínua da escala musical, enquanto Geffen et al. (2025) documentaram  *cimáglifos de interferência*  quando duas frequências musicais são tocadas simultaneamente (como razões de terça menor  \$214\\text{ Hz} \+ 183{,}428\\text{ Hz}\$  ou terça maior  \$214\\text{ Hz} \+ 171{,}2\\text{ Hz}\$ ), produzindo padrões compostos ou dominância de uma frequência sobre a outra. Para integrar essa riqueza à reação em tempo real, o mapeamento áudio-visual segue os princípios validados no sistema  *CymaSense*  de McGowan et al. (2021):  **amplitude**  controla a escala da forma e das partículas,  **altura tonal (**  ***pitch***  **)**  seleciona a geometria cimática e sua luminosidade relativa, e  **timbre**  modula a nitidez da superfície (sons brilhantes com contornos mais agudos, sons escuros com perfis mais arredondados).

##### 4.2 Contrato Canônico do Esquema JSON de Presets

O módulo de dados importado no código Three.js utiliza o catálogo já estruturado no Dossiê Técnico do projeto (cobrindo de  \$20\\text{ Hz}\$  a  \$2000\\text{ Hz}\$ , âncoras experimentais de Chladni/Faraday e a série musical/Solfeggio herdada dos 9 presets de  \$174\\text{ Hz}\$  a  \$852\\text{ Hz}\$  do cimaticlabsanuhazi.html), obedecendo estritamente ao contrato de dez propriedades especificado para o aplicativo.  
Campo JSON,Tipo e Unidade,Papel no Motor Físico e Óptico,Regra de Calibração e Integridade  
hz,Number (Hz),Frequência fundamental do oscilador interno e referência do analisador FFT.,"Faixa contínua de  \$20\\text{ Hz}\$  a  \$2000\\text{ Hz}\$ , incluindo âncoras experimentais e notas musicais/Solfeggio."  
nomeDoDesenho,String,Rótulo descritivo exibido no modal  Atlas Hz  e no indicador de estado.,Descreve a morfologia na Placa de Areia e a simetria correspondente na Água.  
"m, n",Integer,Índices nodais inteiros da Placa de Chladni (Mesa 2\) e da máscara da Mesa 3.,"Deve respeitar  \$m \\ne n\$  sempre que coefA e coefB tiverem sinais opostos, evitando anulação idêntica do campo."  
"coefA, coefB",Number,"Pesos  \$(a, b)\$  da superposição de modos degenerados na placa quadrada.","Alterna continuamente entre grade ortogonal ( \$b=0\$ ), estrela/cruz simétrica ( \$a=b\$ ), antissimétrica ( \$a=-b\$ ) e hipérboles."  
simetriaAgua,Integer ( n-fold ),Ordem azimutal da onda estacionária de Faraday na Mesa 1.,Mapeada das simetrias observadas de 1-fold (anéis) até 48-fold (micro-retículas capilares em  \$2000\\text{ Hz}\$ ).  
tensaoSuperficial,Number ( \$\\text{N/m}\$ ),Tensão superficial  \$\\sigma\$  utilizada para calcular a rigidez capilar  \$\\kappa \= \\sigma H/\\rho\$ .,"Valor nominal do fluido cimático calibrado:  \$0{,}045\\text{ N/m}\$  (contra  \$0{,}0728\\text{ N/m}\$  da água padrão)."  
amortecimentoIdeal,Number ( \$\\text{s}^{-1}\$ ),Taxa de amortecimento  \$\\gamma\_{\\text{base}}\$  no  solver  hidrodinâmico.,Calibrada pela relação de dispersão e limitada para manter estabilidade numérica ( \$\\gamma \\Delta t\_{\\text{sub}} \< 1\$ ).  
anguloLuzRecomendado,Number (graus),Ângulo rasante  \$\\theta\_i\$  inicial sugerido para o anel de LEDs e luzes.,Mantido na janela óptica rasante de  \$75^\\circ\$  a  \$85^\\circ\$  em relação à normal da superfície plana.  
Com o esquema de dados padronizado, o passo seguinte é detalhar os contratos matemáticos e  *shaders*  GLSL que cada motor físico executará sobre esses parâmetros.

#### 5\. Etapa 4 — Contrato Multifísico 3D e Pipeline de Shaders GLSL (WebGL / Three.js)

A passagem definitiva do visual plano para a simulação 3D de alta fidelidade exige implementar quatro motores acoplados com parâmetros fisicamente consistentes, conforme estabelecido na modelagem computacional multifísica do projeto.

##### 5.1 Mesa 1 — Hidrodinâmica de Ponto Focal Central e Resposta Instantânea

Na  **Mesa 1** , o transdutor central único impõe uma condição de velocidade harmônica no pistão central  \$v\_z(r\_0, t) \= V\_0 \\sin(\\omega t)\$ , irradiando ondas cilíndricas descritas por funções de Hankel de primeira espécie  \$H\_m^{(1)}(kr)\$  que refletem na parede da cubeta ( \$R\_m H\_m^{(2)}(kr)\$ ) para formar ondas estacionárias puras. Simultaneamente, o movimento vertical global modula a gravidade efetiva na equação de Mathieu amortecida, selecionando o modo sub-harmônico ( \$\\omega\_f \= \\omega / 2\$ ) acima do limiar crítico  \$a\_c\$ . Conforme demonstrado no  *Phenomena Study \#29* , a não-linearidade do modelo deve combinar um termo quadrático  \$c\_2\$  e um termo cúbico  \$c\_3\$ : quando  \$c\_2 \= 0\$ , a superfície tende a formar apenas listras unidimensionais, enquanto a ativação de  \$c\_2\$  estabiliza redes quadradas e poligonais. Além disso, experimentos de Sheldrake e Sheldrake (2017) confirmam que o tipo de forma de onda (senoidal, quadrada ou triangular) e a temperatura entre  \$5\\,^\\circ\\text{C}\$  e  \$30\\,^\\circ\\text{C}\$  não alteram a morfologia global do padrão, enquanto a redução da profundidade da lâmina reduz drasticamente o Tempo até Expressão Completa (TFE).  
Para resolver o atraso de resposta observado em simulações de água padrão, a Mesa 1 substitui as constantes da água comum em  \$10\\text{ mm}\$  ( \$\\nu \= 1{,}004 \\times 10^{-6}\\text{ m}^2/\\text{s}\$ ,  \$\\sigma \= 0{,}0728\\text{ N/m}\$ ,  \$\\rho \= 998\\text{ kg/m}^3\$ ,  \$\\tau\_{100\\text{Hz}} \= 12{,}5\\text{ s}\$  e  \$\\tau\_{\\text{rise}} \= 250{,}0\\text{ ms}\$ ) pelo  **fluido cimático raso calibrado**  da modelagem computacional: viscosidade cinemática  \$\\nu \= 5{,}50 \\times 10^{-5}\\text{ m}^2/\\text{s}\$ , tensão superficial  \$\\sigma \= 0{,}0450\\text{ N/m}\$ , profundidade  \$H \= 1{,}50\\text{ mm}\$  e densidade  \$\\rho \= 1120\\text{ kg/m}^3\$ . Esse ajuste eleva o amortecimento total  \$\\gamma\_{\\text{total}}(k) \= 2\\nu k^2 \+ \\frac{\\sqrt{\\nu\\omega}}{2H\\sinh(2kH)}\$ , reduzindo o tempo de subida sub-harmônica para  \$\\tau\_{\\text{rise}} \= 1{,}8\\text{ ms}\$  e o tempo de decaimento em  \$100\\text{ Hz}\$  para  \$\\tau\_{100\\text{Hz}} \= 4{,}2\\text{ ms}\$ , garantindo sincronia imediata com voz e música e retorno instantâneo ao espelho liso no silêncio.

##### 5.2 Mesa 2 — Placa de Chladni Livre, Excitação Descentralizada e Travamento Granular

Na  **Mesa 2** , o campo de deslocamento transversal  \$u(x,y)\$  da placa quadrada de lado  \$L\$  com bordas livres é avaliado analiticamente pela superposição degenerada:  
\$\$u(x,y) \= a \\cos\\left(\\frac{n \\pi x}{L}\\right) \\cos\\left(\\frac{m \\pi y}{L}\\right) \+ b \\cos\\left(\\frac{m \\pi x}{L}\\right) \\cos\\left(\\frac{n \\pi y}{L}\\right)\$\$  
Variar  \$\\mu \= b/a\$  transita o desenho de grades ortogonais ( \$b=0\$ ) para cruzes e estrelas diagonais ( \$a=b\$ ), configurações antissimétricas ( \$a=-b\$ ) e hipérboles suaves ( \$0 \< \|\\mu\| \< 1\$ ). Para placas circulares de raio  \$R\$  com borda livre (momento fletor  \$M\_r \= 0\$  e força cortante  \$V\_r \= 0\$ ), a autofunção combina funções de Bessel ordinárias e modificadas  \$w(r,\\theta) \= J\_m(kr) \+ B\_m I\_m(kr)\\cos(m\\theta+\\phi)\$ . Como demonstrado por Lin et al. (2024), quando a excitação é deslocada para fora do centro geométrico ( *off-center driving* ), ocorre multiplicação dos modos ressonantes por estados de máxima entropia — comportamento que pode ser exposto como parâmetro opcional de assimetria.  
Para que os microgrãos de quartzo migrem rapidamente e  **parem sem trepidação artificial**  nas linhas nodais, a física de partículas acopla a difusão heterogênea de Itô (Devauchelle et al., 2026\) ao critério balístico  \$\\Gamma(x,y) \= \|u(x,y)\|\\omega^2 / g\$ :

1. **Deriva acústica e colisões viscoelásticas:**  Os grãos são empurrados dos antinodos em direção aos nós pela força efetiva  \$\\mathbf{F}*{\\text{ac}}(x,y) \= \-2\\alpha \|u(x,y)\|\\nabla\|u(x,y)\|\$ , perdendo energia vertical segundo a restituição  \$e(v*{\\text{rel}}) \= 1 \- c\_e(v\_{\\text{rel}}/v\_0)^{1/5}\$  ( \$c\_e \\approx 0{,}3\$ ) e deslizando sob atrito reológico  \$\\mu(I) \= \\mu\_s \+ \\frac{\\mu\_d \- \\mu\_s}{1 \+ I\_0/I}\$  ( \$\\mu\_s \\approx 0{,}3\$ ).  
2. **Travamento estático na zona morta nodal:**  Conforme documentado por Zhou et al. (2016) e na síntese computacional, aplica-se a probabilidade estocástica de salto  \$P\_{\\text{hop}}(x,y) \= \\max(0, 1 \- \\exp(-\\beta(\\Gamma(x,y) \- 1)))\$ . Sempre que  \$\\Gamma(x,y) \< 1{,}0\$ ,  \$P\_{\\text{hop}}\$  torna-se zero, suprimindo atualizações estocásticas e ancorando o grão de forma estável em  \$u(x,y) \= 0\$ .  
3. **Distinção de regime por tamanho de grão:**  Como observam Aranson e Tsimring (2005) citando Faraday (1831), apenas grãos granulares pesados seguem o acúmulo nodal direto, enquanto pós ultrafinos de  \$10\\text{–}20\\,\\mu\\text{m}\$  migram inversamente aos antinodos por correntes de ar intersticiais; a Mesa 2 opera portanto calibrada no regime granular de quartzo.

##### 5.3 Mesa 3 — Fusão Híbrida em FBO Ping-Pong (RGBA32F), Estabilidade CFL e PML

Na  **Mesa 3** , a superfície líquida é resolvida em  *framebuffers*   *ping-pong*  de ponto flutuante (RGBA32F) por meio da EDP capilar-gravitacional de 4ª ordem para altura  \$h(x,z,t)\$  e velocidade vertical  \$v \= \\partial h / \\partial t\$ :  
\$\$\\frac{\\partial^2 h}{\\partial t^2} \+ 2 \\gamma(x,z) \\frac{\\partial h}{\\partial t} \- c^2 \\nabla^2 h \+ \\kappa \\nabla^4 h \= S(x, z, t)\$\$  
Nesta equação,  \$c \= \\sqrt{gH}\$  é a velocidade de onda rasa gravitacional e  \$\\kappa \= \\sigma H / \\rho\$  é a rigidez capilar. Para que a  **própria geometria nodal de Chladni**  vibre como matriz de micro-alto-falantes submersos emitindo ondas na água, a máscara espacial de excitação é modelada por uma gaussiana centrada no zero nodal ( \$u(x,z) \= 0\$ ):  
\$\$S(x, z, t) \= A\_{\\text{drive}}(t) \\cdot \\cos(\\omega t) \\cdot \\exp\\left( \-\\frac{\|u(x, z)\|^2}{\\varepsilon^2} \\right)\$\$  
Três garantias numéricas asseguram que o desenho central permaneça nítido e estável em WebGL a  \$60\\text{ FPS}\$  ( \$\\Delta t\_{\\text{frame}} \= 16{,}6\\text{ ms}\$ ):

* **Estêncil isotrópico de 9 pontos e integração**  ***Velocity-Verlet***  **:**  O operador Laplaciano  \$\\nabla^2 h\$  aplica pesos  \$4\$  aos vizinhos ortogonais,  \$1\$  aos diagonais e  \$-20\$  ao centro (dividido por  \$6\\Delta x^2\$ ), sendo executado em duas passagens sequenciais para obter o termo bi-harmônico  \$\\nabla^4 h \= \\nabla^2(\\nabla^2 h)\$  sem distorções quadradas de grade.  
* **Sub-stepping estrito pela condição CFL de 4ª ordem:**  Devido ao termo  \$\\kappa \\nabla^4 h\$ , o passo de tempo máximo permitido obedece a  \$\\Delta t\_{\\text{max}} \\le \\frac{\\Delta x^2}{2\\sqrt{\\kappa \+ c^2 \\Delta x^2 / 2}}\$ . O  *loop*  em GPU calcula dinamicamente  \$N\_{\\text{sub}} \= \\lceil \\Delta t\_{\\text{frame}} / \\Delta t\_{\\text{max}} \\rceil\$  sub-passos por quadro, mantendo  \$\\gamma \\Delta t\_{\\text{sub}} \< 1\$  para preservar a estabilidade do amortecimento de Verlet.  
* **Camada Esponja Absorvente (PML Radial):**  Para evitar que as ondas emitidas rebatam nas bordas quadradas do  *framebuffer*  e borrem a geometria central, o amortecimento cresce suavemente na periferia ( \$r\_{\\text{inner}} \= 0{,}85 R\_{\\text{boundary}}\$ ,  \$\\gamma\_{\\text{max}} \\approx 100{,}0\\text{ s}^{-1}\$ ,  \$p \= 3\$ ) conforme  \$\\gamma(x,z) \= \\gamma\_{\\text{base}} \+ \\gamma\_{\\text{max}} \\cdot \\left(\\frac{\\max(0, r(x,z) \- r\_{\\text{inner}})}{R\_{\\text{boundary}} \- r\_{\\text{inner}}}\\right)^p\$ .

##### 5.4 Óptica PBR de Espelho Negro, Iluminação Rasante e Fragment Shader GLSL

O realismo fotográfico da água nas Mesas 1 e 3 segue a geometria óptica do CymaScope e de Hans Jenny: fundo preto fosco (vec3(0.002, 0.003, 0.005)), câmera zenital ( \$\\theta\_c \= 0^\\circ\$ ) e anel circunferencial de LEDs (32 LEDs no instrumento físico, 16 fontes no loop GLSL) posicionado em ângulo rasante  \$\\theta\_i \\in 75^\\circ, 85^\\circ\$  (referência nominal  \$80^\\circ\$ ) com razão altura/diâmetro  \$H\_{\\text{ring}} / D\_{\\text{ring}} \\in 0{,}15, 0{,}35\$  (nominal  \$0{,}25\$ ). As normais são derivadas a cada fragmento por diferenças centrais no  *heightfield* , alimentando o modelo microfaceta GGX ( *Trowbridge-Reitz* ) com rugosidade ultrabaixa ( \$\\alpha \= 0{,}035\$ ), refletância de Fresnel de Schlick e  *tone mapping*  de Reinhard ( \$\\mathbf{C}/(\\mathbf{C}+1)\$ ) contra estouros no centro.  
Para a seleção de materiais citada nos estudos de LearnOpenGL e  *Phenomena Study \#29* , a refletância em incidência normal  \$F\_0\$  varia entre  \$0{,}02\\text{–}0{,}04\$  (água e dielétricos escuros que só brilham em inclinações rasantes) e  \$0{,}56\\text{–}0{,}72\$  (mercúrio negro metálico de contraste duro, além de  \$0{,}62\$  para gálio). Além disso, enquanto o  *shader*  abaixo aplica \-laplacian para realçar linhas cáusticas sobre as cristas ( \$\\nabla^2 h \< 0\$ ), Geffen et al. (2025) observam que, sob o anel superior do CymaScope, vales côncavos refletem luz à câmera e cristas convexas a dispersam; expor essa inversão de sinal como parâmetro óptico permite alternar entre ambos os modos fotográficos. O  *fragment shader*  completo reproduzido da modelagem computacional do projeto implementa essa ótica:  
// GLSL Fragment Shader: Dark-Mirror Cymatic PBR  
uniform sampler2D u\_heightMap;  
uniform vec2 u\_texelSize;  
uniform vec3 u\_cameraPos;  
uniform vec3 u\_ringLightColor;  
uniform float u\_ringRadius;  
uniform float u\_ringHeight;  
uniform float u\_fresnelF0;

varying vec2 v\_uv;  
varying vec3 v\_worldPos;

// Schlick Fresnel Approximation  
vec3 calculateFresnel(float cosTheta, vec3 F0) {  
    return F0 \+ (1.0 \- F0) \* pow(clamp(1.0 \- cosTheta, 0.0, 1.0), 5.0);  
}

// GGX Microfacet Distribution (Specular Highlight)  
float distributionGGX(vec3 N, vec3 H, float roughness) {  
    float a \= roughness \* roughness;  
    float a2 \= a \* a;  
    float NdotH \= max(dot(N, H), 0.0);  
    float NdotH2 \= NdotH \* NdotH;  
    float denom \= (NdotH2 \* (a2 \- 1.0) \+ 1.0);  
    return a2 / (3.14159265 \* denom \* denom);  
}

void main() {  
    // 1\. Compute surface normal from heightfield texture  
    float hL \= texture2D(u\_heightMap, v\_uv \- vec2(u\_texelSize.x, 0.0)).r;  
    float hR \= texture2D(u\_heightMap, v\_uv \+ vec2(u\_texelSize.x, 0.0)).r;  
    float hD \= texture2D(u\_heightMap, v\_uv \- vec2(0.0, u\_texelSize.y)).r;  
    float hU \= texture2D(u\_heightMap, v\_uv \+ vec2(0.0, u\_texelSize.y)).r;  
      
    vec3 N \= normalize(vec3(hL \- hR, 2.0 \* u\_texelSize.x, hD \- hU));  
    vec3 V \= normalize(u\_cameraPos \- v\_worldPos);  
      
    // 2\. Compute second-order curvature for optical caustics modulation  
    float laplacian \= (hL \+ hR \+ hD \+ hU \- 4.0 \* texture2D(u\_heightMap, v\_uv).r);  
    float curvatureFocus \= clamp(-laplacian \* 15.0, 0.0, 2.5);  
      
    // Base dark dielectric fluid absorption  
    vec3 baseColor \= vec3(0.002, 0.003, 0.005);  
    vec3 finalColor \= baseColor;  
      
    // 3\. Accumulate specular reflections over LED Ring Light array  
    vec3 F0 \= vec3(u\_fresnelF0); // Water: 0.02, Black Mercury: 0.56  
    float roughness \= 0.035;    // Ultra-smooth mirror finish  
      
    for (int i \= 0; i \< 16; i++) {  
        float angle \= float(i) \* (6.2831853 / 16.0);  
        vec3 lightPos \= vec3(cos(angle) \* u\_ringRadius, u\_ringHeight, sin(angle) \* u\_ringRadius);  
        vec3 L \= normalize(lightPos \- v\_worldPos);  
        vec3 H \= normalize(V \+ L);  
          
        float NdotL \= max(dot(N, L), 0.0);  
        float NdotV \= max(dot(N, V), 0.0);  
          
        vec3 F \= calculateFresnel(max(dot(H, V), 0.0), F0);  
        float D \= distributionGGX(N, H, roughness);  
          
        // Specular reflection highlight  
        vec3 specular \= (D \* F) / (4.0 \* NdotV \* NdotL \+ 0.001);  
          
        // Modulate highlight intensity via grazing angle and curvature focus  
        finalColor \+= specular \* u\_ringLightColor \* NdotL \* (1.0 \+ curvatureFocus);  
    }  
      
    // Tone mapping to prevent center washout  
    finalColor \= finalColor / (finalColor \+ vec3(1.0));  
    gl\_FragColor \= vec4(pow(finalColor, vec3(1.0 / 2.2)), 1.0);  
}

Somado ao anel rasante, o sistema preserva as  **Luzes Customizadas arrastáveis via**  **Raycaster**  com controles de posição X/Z, altura Y (referência inicial yPos \= 1.4 para raios), ângulo e decaimento distance calibrado do cimatic4mesatopluzfraca.html, além do deslocamento horizontal X/Z de vértices ( *Fluido/Mercúrio*  do cimatic5.html) para reforçar a tridimensionalidade física. Definidos todos os contratos matemáticos e ópticos, a última etapa organiza a execução prática nos geradores de código.

#### 6\. Etapa 5 — Pacote de Execução em 4 Fases para Argon e Hydrogen

Enviar toda a especificação de uma só vez ao Argon ou ao Hydrogen aumenta o risco de simplificação dos  *shaders*  FBO para equações 2D estáticas ou de regressão na interface. O build deve ser conduzido em quatro fases sequenciais, validando cada critério de aceite antes de liberar a fase seguinte.

##### 6.1 Fase A: Fundação Arquitetural, Cena Three.js 3D e Sidebar em Camadas

Esta primeira fase cria o palco 3D limpo, a câmera orbital e a estrutura de navegação em camadas sem acoplar ainda equações pesadas de fluido ou partículas.  
**Prompt de Execução — Fase A (Argon / Hydrogen):**  Crie a estrutura modular do aplicativo  *Cymatics Studio Master*  em Three.js / WebGL com cena 3D de câmera zenital e rotação/zoom orbital suave sobre uma mesa central intercambiável (circular ou quadrada, baseada na malha  \$18\\times 18\$  sobre fundo preto absoluto). Implemente a interface em glass-ui escuro com tipografia dourada/violeta de alto contraste organizada em exatamente três elementos estruturais: (1) barra superior compacta contendo o seletor exclusivo das 3 Mesas ( *Mesa 1: Água Pura CymaScope* ,  *Mesa 2: Placa de Chladni* ,  *Mesa 3: Fusão Híbrida* ), 4 botões de Assinatura Clássica de 1 clique ( *Cimatic 3 Espelho Negro* ,  *Cimatic 4 Luz Suave* ,  *Cimatic 6 VJ DJ* ,  *Água Fluida* ) e botão  *Modo Sessão* ; (2) Sidebar lateral única com 5 botões de camada ( *Áudio & Mixer* ,  *Física da Mesa* ,  *Luzes & Óptica* ,  *Atlas Hz* ,  *VJ & Sessão* ), onde clicar em qualquer botão abre exclusivamente seu modal contextual dentro da própria sidebar e recolhe os demais; (3) indicador de estado mínimo exibindo frequência atual em Hz, índices nodais  \$(m,n)\$  e simetria ativa. Proibido espalhar botões soltos fora da barra superior e da sidebar.  
A entrega da Fase A é aprovada quando as três abas de mesa e os cinco modais contextuais alternam sem sobreposição visual, mantendo a área principal de visualização 3D livre de obstrução por painéis longos e com resposta orbital fluida.

##### 6.2 Fase B: Motor Web Audio API, Atlas de Frequências JSON e Mapeamento Espectral

A segunda fase conecta o processamento sonoro em tempo real e o catálogo de frequências como fonte única de parâmetros físicos para as três mesas.  
**Prompt de Execução — Fase B (Argon / Hydrogen):**  Implemente o módulo AudioEngine via Web Audio API suportando três fontes alternáveis: Microfone ao vivo, Upload/Player de Áudio e Oscilador Senoidal Interno com  *fade-in*  e  *fade-out*  suaves sem estalos. Inclua Volume Master, Filtro LowPass em tempo real com slider contínuo de frequência de corte ( \$50\\text{ Hz}\$  a  \$2000\\text{ Hz}\$ ), detector de frequência dominante via FFT, detector de picos de energia (energyPeak) com indicador visual LED de batida e medidor de estabilidade harmônica ( *Harmonic Resonance* ). Integre o catálogo CYMATICS\_PRESETS (cobrindo de  \$20\\text{ Hz}\$  a  \$2000\\text{ Hz}\$ , âncoras experimentais de Chladni/Faraday e a série musical/Solfeggio incluindo os 9 presets de  \$174\\text{ Hz}\$  a  \$852\\text{ Hz}\$ ) dentro do modal  *Atlas Hz* , garantindo que cada item contenha { hz, nomeDoDesenho, m, n, coefA, coefB, simetriaAgua, tensaoSuperficial, amortecimentoIdeal, anguloLuzRecomendado }. Aplique mapeamento áudio-visual contínuo inspirado no  *CymaSense*  (amplitude controla escala,  *pitch*  controla modo geométrico e luminosidade relativa, e conteúdo espectral/timbre modula nitidez dos contornos).  
A entrega da Fase B é aprovada quando o oscilador interno alterna entre frequências sem cliques audíveis, o filtro LowPass altera em tempo real a leitura FFT e o silêncio zera o envelope de amplitude sem atraso perceptível.

##### 6.3 Fase C: Solvers 3D das Mesas 1 e 2, Óptica de Espelho Negro e Luzes Arrastáveis X/Y/Z

A terceira fase consolida o salto visual para 3D, construindo as duas primeiras mesas de forma independente e validando a óptica pura de reflexo antes do acoplamento híbrido.  
**Prompt de Execução — Fase C (Argon / Hydrogen):**  Implemente os motores 3D e a óptica das Mesas 1 e 2\. Na  **Mesa 1 (Água Pura / CymaScope)** , modele excitação por ponto focal central único ( \$r=0\$ , interferência radial  \$H\_m^{(1)} \+ R\_m H\_m^{(2)}\$  combinada à instabilidade sub-harmônica  \$f\_0/2\$  de Faraday com termos não-lineares quadrático  \$c\_2\$  e cúbico  \$c\_3\$ ) usando o fluido raso calibrado ( \$\\nu \= 5{,}50 \\times 10^{-5}\\text{ m}^2/\\text{s}\$ ,  \$\\sigma \= 0{,}0450\\text{ N/m}\$ ,  \$H \= 1{,}50\\text{ mm}\$ ,  \$\\rho \= 1120\\text{ kg/m}^3\$ ) para atingir resposta rápida ( \$\\tau\_{\\text{rise}} \= 1{,}8\\text{ ms}\$ ) e retorno imediato ao espelho plano no silêncio ( \$\\tau\_{100\\text{Hz}} \= 4{,}2\\text{ ms}\$ ). Renderize a superfície com o  *fragment shader*  GLSL PBR de Espelho Negro (emissiveIntensity \= 0, normais dinâmicas por diferenças centrais  \$\\nabla h\$ , Fresnel de Schlick alternável entre água dielétrica  \$F\_0 \= 0{,}02\\text{–}0{,}04\$  e mercúrio negro  \$F\_0 \= 0{,}56\\text{–}0{,}72\$ , GGX roughness \= 0.035, foco de curvatura  \$-\\nabla^2 h\$  com opção de inversão para vales brilhantes e  *tone mapping*  Reinhard), iluminado por um anel de 16 a 32 LEDs em ângulo rasante ( \$\\theta\_i \= 75^\\circ\\text{–}85^\\circ\$ ,  \$H\_{\\text{ring}}/D\_{\\text{ring}} \\approx 0{,}25\$ ) somado às Luzes Customizadas arrastáveis via Raycaster com controles explícitos de posição X/Z, altura Y (yPos \= 1.4 inicial), ângulo e alcance distance calibrado. Na  **Mesa 2 (Placa de Chladni)** , simule a chapa 3D quadrada (superposição degenerada  \$(a,b)\$ ) e circular (funções de Bessel  \$J\_m \+ B\_m I\_m\$ ) com milhares de microgrãos de areia impelidos por  \$\\mathbf{F}*{\\text{ac}} \= \-2\\alpha\|u\|\\nabla\|u\|\$ , restituição  \$e(v*{\\text{rel}})\$  e travamento estático estrito ( \$P\_{\\text{hop}} \= 0\$  quando  \$\\Gamma \= \|u\|\\omega^2/g \< 1{,}0\$ ) para que parem imóveis nas linhas nodais sem tremer. Adicione no modal  *Luzes & Óptica*  o seletor de acabamento ( *Espelho Negro Cimatic 3* ,  *Luz Suave Cimatic 4* ,  *Anuhazi Emissivo* ), o deslocamento horizontal X/Z ( *Fluido/Mercúrio* ) e os 33 raios radiais com coreografias ( *8 Loop* ,  *Vortex* ,  *Salto* ,  *Arco-Íris* ,  *Hz Color* ), além de sliders de velocidade e foco dos raios.  
A entrega da Fase C é aprovada quando a Mesa 1 apresenta superfície negra lisa sem emissão artificial nem estouro branco no centro durante o silêncio, as luzes arrastáveis alteram X/Z, altura Y e reflexo especular sobre as cristas 3D, e os grãos da Mesa 2 assentam sem tremor visível sobre cruz ortogonal, estrela diagonal ou hipérboles conforme  \$(a,b)\$  varia.

##### 6.4 Fase D: Mesa 3 Híbrida (Chladni → Heightfield FBO 3D) e Integração VJ / Modo Sessão

A quarta e última fase acopla a geometria nodal sólida como fonte acústica distribuída no  *solver*  fluido em GPU e finaliza os recursos de performance e imersão.  
**Prompt de Execução — Fase D (Argon / Hydrogen):**  Implemente a  **Mesa 3 (Fusão Cimática Híbrida)**  acoplando o campo escalar  \$u(x,z)\$  da Placa de Chladni a um  *solver*  de EDP capilar-gravitacional 2D de 4ª ordem ( \$\\partial^2 h/\\partial t^2 \+ 2\\gamma\\partial h/\\partial t \- c^2\\nabla^2 h \+ \\kappa\\nabla^4 h \= S(x,z,t)\$ ) executando em  *framebuffers*   *ping-pong*  RGBA32F de alta resolução (evoluindo a grade  \$161\\times 161\$  do cimaticaguafluida.html). Utilize estêncil Laplaciano isotrópico de 9 pontos em duas passagens para  \$\\nabla^4 h\$ , integração  *Velocity-Verlet*  com  *sub-stepping*  dinâmico pela condição CFL de 4ª ordem ( \$N\_{\\text{sub}} \= \\lceil \\Delta t\_{\\text{frame}} / \\Delta t\_{\\text{max}} \\rceil\$ , com  \$\\Delta t\_{\\text{max}} \\le \\Delta x^2 / (2\\sqrt{\\kappa \+ c^2\\Delta x^2/2})\$  e  \$\\gamma \\Delta t\_{\\text{sub}} \< 1\$ ), camada esponja radial absorvente PML ( \$r\_{\\text{inner}} \= 0{,}85 R\_{\\text{boundary}}\$ ,  \$\\gamma\_{\\text{max}} \= 100{,}0\\text{ s}^{-1}\$ ,  \$p \= 3\$ ) e máscara de excitação gaussiana centrada nas linhas nodais  \$S(x,z,t) \= A\_{\\text{drive}}(t)\\cos(\\omega t)\\exp(-\|u(x,z)\|^2/\\varepsilon^2)\$  para que a própria figura nodal emita micro-ondas concêntricas sobre o shader PBR de Espelho Negro sem borrar a geometria central. Integre também o botão  *Estabilização Cimática*  (persistenceFactor), a opção de usar luzes arrastáveis como emissores multi-ponto na água física, os 6 nós de cor/viscosidade (0.940 Rubi a 0.985 Violeta), o  *AI Visual DJ*  por energyPeak (disparando Caleidoscópio, raios e as  \$4.000\$  partículas em AdditiveBlending nos picos sonoros) e o  *Modo Sessão*  com cronômetro e bloqueio de cliques acidentais, conectando os 4 botões de Assinatura Clássica ao estado completo.  
A entrega da Fase D é aprovada quando a Mesa 3 exibe com nitidez um padrão nodal pulsante (como cruz, estrela ou mandala) irradiando ondas laterais que se extinguem suavemente na camada PML sem reflexos de borda, mantendo estabilidade numérica em 60 FPS e alternando instantaneamente entre as quatro Assinaturas Clássicas.  
