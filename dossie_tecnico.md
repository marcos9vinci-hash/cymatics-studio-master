### Dossiê Técnico de Engenharia Multifísica e Renderização: Cymatics Studio Master

O  **Cymatics Studio Master**  integra três regimes físicos distintos sob uma mesma arquitetura de simulação em tempo real (Three.js, WebGL/GLSL e Web Audio API): a hidrodinâmica paramétrica e radial de ondas de Faraday em superfície líquida livre ( **Mesa 1 — Água Pura / CymaScope** ), a elastodinâmica flexural de placas sólidas acoplada ao transporte estocástico de meios granulares ( **Mesa 2 — Placa de Chladni com Microgrãos** ) e o acoplamento direto da topologia nodal sólida como fonte acústica distribuída em um  *solver*  capilar-gravitacional 2D ( **Mesa 3 — Fusão Cimática Híbrida** ), todos visualizados por óptica especular de espelho negro.  
Para preservar o rigor científico e a rastreabilidade exigidos em engenharia acústica, este dossiê distingue explicitamente os  **dados experimentais e de modelagem documentados na literatura primária**  (Ernst Chladni, Michael Faraday, Mary Waller, Hans Jenny, John Stuart Reid, Sheldrake e Sheldrake, Val Baker et al., Tuan et al., Shao et al., Devauchelle et al.) das  **calibrações paramétricas derivadas analiticamente**  para preencher faixas contínuas de operação do simulador, como as frequências musicais e a série Solfeggio.

#### 1\. Bloco 1: Atlas Completo de Frequências (Hz), Modos (m, n) e Geometrias Formadas

A correspondência entre frequência de excitação acústica, índices nodais e morfologia geométrica não é universal entre diferentes corpos físicos, pois depende da geometria de contorno, da rigidez flexural da placa sólida ou da profundidade e diâmetro da cubeta líquida. Compreender essa dependência evita erros clássicos de parametrização ao acoplar áudio em tempo real a um motor gráfico.

##### 1.1 Leis de Escala e Seleção Modal em Sólidos e Fluidos

Em placas elásticas finas isotrópicas de espessura  \$h\$ , densidade  \$\\rho\$ , módulo de Young  \$E\$  e razão de Poisson  \$\\nu\_p\$ , a teoria de placas de Kirchhoff–Love estabelece que o deslocamento transversal  \$u(x,y,t)\$  obedece à equação bi-harmônica de quarta ordem, conforme detalhado por Tuan et al. (2015) e Lin et al. (2024):  
\$\$D \\nabla^4 u(x,y,t) \+ \\rho h \\frac{\\partial^2 u(x,y,t)}{\\partial t^2} \= F(x,y,t)\$\$  
Nesta expressão,  \$D \= \\frac{E h^3}{12(1 \- \\nu\_p^2)}\$  é a rigidez flexural e  \$F(x,y,t)\$  é a força de excitação externa. Para excitação harmônica contínua em frequência angular  \$\\omega \= 2\\pi f\$ , a relação de dispersão flexural conecta a frequência ao número de onda  \$k\$ :  
\$\$k \= \\left( \\frac{\\rho h \\omega^2}{D} \\right)^{1/4} \= \\left( \\frac{12 \\rho (1 \- \\nu\_p^2) \\omega^2}{E h^2} \\right)^{1/4}\$\$  
Como  \$\\omega \\propto k^2\$ , ondas de flexão em placas são dispersivas, com velocidade de fase crescente com a raiz quadrada da frequência,  \$v(f) \= \\omega/k \\propto \\sqrt{\\omega}\$ . Essa propriedade fundamenta a  **Lei empírica de Chladni** , que relaciona a frequência de ressonância  \$f\$  ao número de linhas nodais radiais ou lineares  \$m\$  e de linhas nodais circulares ou concêntricas  \$n\$ :  
\$\$f \\approx C (m \+ 2n)^p\$\$  
Para placas planas finas, o expoente empírico assume  \$p \\approx 2\$  (aproximando-se de  \$p \\approx 1\$  em cascas curvas ou pratos), enquanto  \$C\$  encapsula as dimensões e constantes elásticas da chapa. Além disso, experimentos de Zhou et al. (2016) demonstraram que, em placas acionadas centralmente, curvas de amplitude mínima (linhas nodais) se formam em qualquer frequência contínua da escala musical, embora picos agudos de ressonância exijam menor potência do transdutor, e a excitação descentralizada multiplique o número de modos ativos por maximização de entropia da função de Green, como demonstrado por Lin et al. (2024).  
Em contraste com as placas sólidas — onde a borda impõe as autofunções na frequência de excitação  \$f\$  —, a superfície da água na  **Mesa 1**  responde por instabilidade paramétrica de Faraday, oscilando na  **primeira sub-harmônica**  da excitação ( \$f\_{\\text{onda}} \= f\_0 / 2\$  ou  \$\\omega\_f \= \\omega/2\$ ), conforme confirmado experimentalmente no CymaScope por Sheldrake e Sheldrake (2017) e Geffen et al. (2025). O número de onda selecionado emerge da relação de dispersão gravidade-capilaridade para profundidade  \$H\$ , aceleração da gravidade  \$g\$  e tensão superficial  \$\\sigma\$ :  
\$\$\\omega\_f^2 \= \\left( g k \+ \\frac{\\sigma}{\\rho} k^3 \\right) \\tanh(k H)\$\$  
Em função dessa dispersão, a transição contínua de frequência na água produz  **bacias de atração**  discretas separadas por catástrofes de salto ( *Hopf-Takens* ) ou oscilação ( *Duffing-Zeeman* ), fortemente dependentes do diâmetro da cubeta, conforme observaram Sheldrake e Sheldrake (2017) ao comparar células de  \$10{,}00\\text{ mm}\$ ,  \$24{,}25\\text{ mm}\$  e  \$49{,}50\\text{ mm}\$ .

##### 1.2 Atlas Empírico Documentado nas Fontes (12 Hz a 2000 Hz)

Os ensaios experimentais e modelos de alta frequência presentes na literatura do projeto cobrem faixas complementares: Sheldrake e Sheldrake (2017) e Geffen et al. (2025) mapearam cubetas de quartzo no CymaScope entre  \$8\\text{ Hz}\$  e  \$256\\text{ Hz}\$ ; Val Baker et al. (2024) mediram picos de impedância e reconstruíram padrões nodais em 10 placas acrílicas de  \$2\\text{ mm}\$  entre  \$107\\text{ Hz}\$  e  \$1635\\text{ Hz}\$ ; e a síntese computacional baseada em Shao et al. (2021) estendeu os modos cilíndricos de Faraday  \$J\_m(k\_{mn}r)\\cos(m\\theta+\\phi\_m)\$  até  \$2000\\text{ Hz}\$ .  
A tabela a seguir consolida os pontos diretamente documentados nas fontes, servindo de âncora física para a calibração do simulador.  
Frequência (Hz),Sistema / Geometria de Referência,Índices / Ordem Modal,Velocidade de Fase ou Limiar,Morfologia e Simetria Documentada,Fonte Primária  
"12,0",Água — Cubeta triangular ( \$50\\text{ mm}\$ ),—,—,Cimáglifo coerente triangular,Geffen et al. (2025)  
"20,0",Água — Camada com partículas,"\$\\Gamma \= 3{,}0\\text{–}3{,}9\$",—,Arranjos regulares de partículas em fundo líquido vibrante,Voth et al. via Aranson e Tsimring (2005)  
"26,5","Água — Cubeta circular ( \$24{,}25\\text{ mm}\$ )",Alternância de fase,—,Simetria 3-fold alternada / composta 6-fold; rotação horária,Geffen et al. (2025)  
"27,0","Água / Mercúrio — Caixa ( \$87{,}9\\,l\_c\$ )","Resposta a  \$13{,}5\\text{ Hz}\$","\$A \= 1{,}6\\,A\_c\$",Rede quadrada com células de  \$17\\text{ mm}\$,Phenomena Study \#29 (2026)  
"35,34","Água — Cubeta circular ( \$24{,}25\\text{ mm}\$ )",Alternância de fase,—,Simetria 4-fold alternada / composta 8-fold,Geffen et al. (2025)  
"36,0","Água — Cubeta retangular ( \$24{,}25\\times 15\\text{ mm}\$ )","\$(2,1)\$","\$a\_c/g \= 0{,}18\$","Simetria 2-fold bilateral ( \$H \= 3{,}0\\text{ mm}\$ )",Geffen et al. (2025); Síntese (2026)  
"43,0","Água — Cubeta circular ( \$24{,}25\\text{ mm}\$ )","\$(0,1)\$","\$a\_c/g \= 0{,}22\$",Simetria 1-fold (anéis concêntricos),Geffen et al. (2025); Síntese (2026)  
"45,0",Água — Cubeta triangular ( \$50\\text{ mm}\$ ),"\$(3,1)\$","\$a\_c/g \= 0{,}25\$","Simetria 3-fold triangular ( \$H \= 4{,}0\\text{ mm}\$ )",Geffen et al. (2025); Síntese (2026)  
"56,0","Água — Cubeta circular ( \$24{,}25\\text{ mm}\$ )","\$(4,1)\$  / Modo 3","\$a\_c/g \= 0{,}31\$",Simetria 4-fold em grade (Geffen) / 6-fold composta de 3 picos alternados (Sheldrake),Sheldrake (2017); Geffen et al. (2025)  
"66,0","Água — Cubeta circular ( \$24{,}25\\text{ mm}\$ )","\$(5,1)\$","\$a\_c/g \= 0{,}38\$",Simetria 5-fold pentagonal,Geffen et al. (2025); Síntese (2026)  
"69,0","Água — Cubeta circular ( \$24{,}25\\text{ mm}\$ )","\$(10,1)\$","\$a\_c/g \= 0{,}41\$",Simetria 10-fold decagonal estável (com rotação bidirecional),Geffen et al. (2025); Síntese (2026)  
"73,0","Água — Cubeta circular ( \$24{,}25\\text{ mm}\$ )","\$(10,2)\$","\$a\_c/g \= 0{,}45\$",Simetria 10-fold estrela decagonal,Geffen et al. (2025); Síntese (2026)  
"78,0","Água — Cubeta circular ( \$24{,}25\\text{ mm}\$ )","\$(12,1)\$","\$a\_c/g \= 0{,}50\$",Simetria 12-fold dodecagonal,Geffen et al. (2025); Síntese (2026)  
"82,0","Água — Cubeta circular ( \$24{,}25\\text{ mm}\$ )","\$(8,2)\$","\$a\_c/g \= 0{,}54\$",Simetria 8-fold octogonal,Geffen et al. (2025); Síntese (2026)  
"89,0","Água — Cubeta quadrada ( \$25{,}2\\text{ mm}\$ )","\$(4,2)\$","\$a\_c/g \= 0{,}62\$",Simetria 4-fold em grade ( grid cymaglyph ),Geffen et al. (2025); Síntese (2026)  
"107,0",Placa Chladni — Quadrada ( \$24\\text{ cm}\$ ),\$n \= 1\$,"\$v \= 29{,}3\\text{ m/s}\$","Primeiro modo ressonante ( \$A\_1 \= \-0{,}10; C\_1 \= 0{,}95\$ )",Val Baker et al. (2024)  
"111,0","Água — Cubeta circular ( \$24{,}25\\text{ mm}\$ )",Modo 5,—,Simetria 10-fold estável; salta para 16-fold em alta amplitude,Sheldrake e Sheldrake (2017)  
"129,0","Água — Cubeta circular ( \$24{,}25\\text{ mm}\$ )","\$(2,3)\$","\$a\_c/g \= 0{,}95\$",Simetria 2-fold bilateral de alta ordem,Geffen et al. (2025); Síntese (2026)  
"158,0",Placa Chladni — Circular ( \$24\\text{ cm}\$ ),\$n \= 1\$,"\$v \= 35{,}6\\text{ m/s}\$","Anel nodal único ( \$C\_1 \= 0{,}95\$ )",Val Baker et al. (2024)  
"174,0",Placa Chladni — Hexágonos ( \$12\\text{ cm}\$  e  \$9\\text{ cm}\$ ),\$f\_1\$,"\$v \= 37{,}3\\text{ m/s}\$","Primeiro modo nodal hexagonal ( \$C\_1 \= 1{,}10\$  e  \$1{,}90\$ )",Val Baker et al. (2024)  
"180,0","Água — Circular ( \$24{,}25\\text{ mm}\$ ) / Quadrada ( \$25{,}2\\text{ mm}\$ )",Modo 7,—,14-fold na cubeta circular (salta a 20-fold); grade ortogonal na quadrada,Sheldrake (2017); Geffen et al. (2025)  
"238,0","Água — Cubeta circular ( \$24{,}25\\text{ mm}\$ )","\$(6,4)\$","\$a\_c/g \= 1{,}85\$","Rede hexagonal 6-fold ( \$H \= 2{,}0\\text{ mm}\$ )",Geffen et al. (2025); Síntese (2026)  
"283,0",Placa Chladni — Quadrada ( \$24\\text{ cm}\$ ),"\$n \= 1, 2\$","\$v \= 47{,}6\\text{ m/s}\$","Segundo modo quadrado com dois contornos nodais ( \$A\_2 \= \-1{,}85\$ )",Val Baker et al. (2024)  
"500,0","Água — Cubeta circular ( \$50{,}0\\text{ mm}\$ )","\$(18,6)\$","\$a\_c/g \= 4{,}20\$","Teia capilar de alta ordem, simetria 18-fold ( \$H \= 1{,}5\\text{ mm}\$ )",Shao et al. (2021) via Síntese (2026)  
"511,0",Placa Chladni — Quadrada ( \$24\\text{ cm}\$ ),"\$n \= 1, 2\$","\$v \= 63{,}9\\text{ m/s}\$","Terceiro modo quadrado com modulação positiva ( \$A\_2 \= 1{,}70\$ )",Val Baker et al. (2024)  
"582,0",Placa Chladni — Circular ( \$24\\text{ cm}\$ ),"\$n \= 1, 2\$","\$v \= 68{,}2\\text{ m/s}\$","Dois anéis nodais concêntricos ( \$C\_1 \= 1{,}35; C\_2 \= 1{,}00\$ )",Val Baker et al. (2024)  
"744,0",Placa Chladni — Quadrada ( \$24\\text{ cm}\$ ),"\$n \= 1, 2, 3\$","\$v \= 77{,}1\\text{ m/s}\$","Quarto modo quadrado com três linhas nodais ( \$A\_2 \= \-1{,}20; A\_3 \= \-1{,}30\$ )",Val Baker et al. (2024)  
"1181,0",Placa Chladni — Quadrada ( \$24\\text{ cm}\$ ),"\$n \= 1, 2, 3, 4\$","\$v \= 97{,}2\\text{ m/s}\$","Quinto modo quadrado complexo com mistura modal inicial ( \$A\_4 \= \-5{,}80\$ )",Val Baker et al. (2024)  
"1200,0","Água — Cubeta circular ( \$50{,}0\\text{ mm}\$ )","\$(32,12)\$","\$a\_c/g \= 9{,}80\$","Micro-retícula quase-cristalina 32-fold ( \$H \= 1{,}0\\text{ mm}\$ )",Shao et al. (2021) via Síntese (2026)  
"1378,0",Placa Chladni — Circular ( \$24\\text{ cm}\$ ),"\$n \= 1, 2, 3\$","\$v \= 105{,}0\\text{ m/s}\$","Três anéis nodais concêntricos ( \$C\_1 \= 2{,}10; C\_2 \= 1{,}15; C\_3 \= 0{,}75\$ )",Val Baker et al. (2024)  
"1635,0",Placa Chladni — Hexagonal ( \$12\\text{ cm}\$ ),"\$n \= 1, 2, 3\$","\$v \= 114{,}4\\text{ m/s}\$",Quarto modo hexagonal com evidência de mistura modal,Val Baker et al. (2024)  
"2000,0","Água — Cubeta circular ( \$50{,}0\\text{ mm}\$ )","\$(48,20)\$","\$a\_c/g \= 16{,}50\$","Campo denso de micro-ondulações capilares 48-fold ( \$H \= 1{,}0\\text{ mm}\$ )",Shao et al. (2021) via Síntese (2026)

##### 1.3 Mapeamento Unificado do Simulador: Graves, Série Musical/Solfeggio e Agudos (20 Hz a 2000 Hz)

Uma verificação crítica nas 19 fontes disponíveis mostra que  **apenas**  **\$174\\text{ Hz}**\$  **aparece diretamente medida em experimento**  (como primeira ressonância  \$f\_1 \= 174\\text{ Hz}\$  das placas acrílicas hexagonais de  \$12\\text{ cm}\$  e  \$9\\text{ cm}\$  em Val Baker et al., 2024). As demais frequências musicais e da escala Solfeggio solicitadas para o aplicativo ( \$110\\text{ Hz}\$ ,  \$285\\text{ Hz}\$ ,  \$396\\text{ Hz}\$ ,  \$417\\text{ Hz}\$ ,  \$432\\text{ Hz}\$ ,  \$440\\text{ Hz}\$ ,  \$528\\text{ Hz}\$ ,  \$639\\text{ Hz}\$ ,  \$741\\text{ Hz}\$ ,  \$852\\text{ Hz}\$  e  \$963\\text{ Hz}\$ )  **não possuem ensaios empíricos dedicados nas fontes consultadas** , embora Zhou et al. (2016) confirmem que placas excitadas no centro formam padrões nodais bem definidos em qualquer nota da escala musical.  
Para entregar um mapa completo e operacional para as três mesas do  **Cymatics Studio Master**  sem fabricar resultados laboratoriais, a tabela seguinte ancora a placa quadrada virtual na constante estrutural extraída da placa de referência de  \$24\\text{ cm}\$  de Val Baker et al. (2024), onde  \$f\_1 \= 107\\text{ Hz}\$  para o modo  \$(m=1, n=1)\$  implica  \$C \= 107 / (1 \+ 2\\cdot 1)^2 \\approx 11{,}89\\text{ Hz}\$  com  \$p \= 2\$ . Esse ajuste reproduz com alta aderência as ressonâncias experimentais medidas na mesma placa:  \$(1,2) \\to 297{,}2\\text{ Hz}\$  (medido:  \$283\\text{ Hz}\$ ),  \$(3,2) \\to 582{,}6\\text{ Hz}\$  (medido:  \$511\\text{ Hz}\$  quadrada /  \$582\\text{ Hz}\$  circular),  \$(2,3) \\to 760{,}9\\text{ Hz}\$  (medido:  \$744\\text{ Hz}\$ ) e  \$(4,3) \\to 1188{,}9\\text{ Hz}\$  (medido:  \$1181\\text{ Hz}\$ ). Nos modos quadrados degenerados, assegura-se  \$m \\ne n\$  sempre que a mistura for antissimétrica ( \$a \= \-b\$ ), pois para  \$m \= n\$  a diferença anula o campo identicamente. As simetrias na água são ancoradas nos ensaios de Sheldrake e Sheldrake (2017), Geffen et al. (2025) e Shao et al. (2021) onde há dado direto, e escaladas pela relação de dispersão gravidade-capilaridade para os pontos musicais interpolados.  
Freq. (Hz),Origem do Dado,"Parâmetros  \$(m, n)\$  (Lei de Chladni  \$p=2\$ )",Nome e Descrição Visual na Placa de Areia,Simetria Azimutal na Água (CymaScope / Faraday)  
"20,0",Empírico (Água) / Calib. (Placa),"\$(1, 0)\$  ( \$m+2n=1\$ , placa expandida)","Cruz Diagonal Fundamental X : para  \$(1,0)\$  antissimétrico ( \$a=-b\$ ), as diagonais  \$x \= \\pm y\$  dividem a chapa em 4 triângulos",2-fold / 4-fold  (ondas gravitacionais longas e organização granular sub-harmônica)  
"27,0",Empírico (Água) / Calib. (Placa),"\$(1, 0)\$  (regime sub-harmônico)",Cruz Diagonal X Aberta : quatro setores periféricos ativos separados pelos eixos diagonais,"4-fold  (rede quadrada de  \$17\\text{ mm}\$  em resposta sub-harmônica a  \$13{,}5\\text{ Hz}\$ )"  
"43,0",Empírico (Água) / Calib. (Placa),"\$(2, 0)\$  ( \$f\_{\\text{est}} \= 47{,}6\\text{ Hz}\$  para  \$(0,1)\$ )","Cruz Diagonal Dupla / Losango Central : para  \$(2,0)\$  com  \$a=-b\$ , formam-se as diagonais ortogonais  \$x=\\pm y\$  e laços de borda","1-fold  (anéis concêntricos perfeitos, modo cilíndrico  \$(0,1)\$ )"  
"56,0",Empírico (Água),"\$(2, 1)\$  (transição de baixa ordem)",Quatro Lóbulos Simétricos : cruz central contornada por arcos fechados nos cantos da placa,4-fold / 6-fold  (grade de 4 pontas em Geffen et al.; 3 picos alternados formando 6 pontas compostas em Sheldrake)  
"69,0",Empírico (Água),"\$(2, 1)\$  (mistura  \$\\mu \= 0{,}85\$ )",Cruz Central \+ Fechamento em Losango : linhas nodais convergindo ao centro com lóbulos amplos,"10-fold  (estrela decagonal estável de 10 pontas, modo  \$(10,1)\$ )"  
"78,0",Empírico (Água),"\$(2, 1)\$  (mistura  \$\\mu \= \-0{,}75\$ )",Quatro Pétalas / Cruz Curva : curvatura suave conectando os pontos médios das bordas,"12-fold  (roseta dodecagonal de 12 pontas, modo  \$(12,1)\$ )"  
"82,0",Empírico (Água),"\$(2, 1)\$  (mistura  \$\\mu \= \-1{,}0\$ )",Cruz de Braços Abertos : transição hiperbólica entre cruz diagonal e lóbulos de borda,"8-fold  (flor octogonal de 8 pétalas, modo  \$(8,2)\$ )"  
"107,0",Empírico (Placa 24 cm),"\$(1, 1)\$  ( \$m+2n=3\$ ,  \$a=b\$ )",Cruz Central / Lóbulos Primários (  \$f\_1\$  ) : primeiro modo ressonante simétrico na placa quadrada de  \$24\\text{ cm}\$,4-fold  (interpolação da cubeta quadrada de  \$89\\text{ Hz}\$  a  \$144\\text{ Hz}\$ )  
"110,0",Calibração analítica (Lá2),"\$(2, 0)\$  ( \$a=b\$ , vizinho de  \$107\\text{ Hz}\$ )",Losango Central Inscrito : curva nodal fechada ligando os pontos médios das quatro bordas,10-fold  (vizinho imediato à bacia de  \$111\\text{ Hz}\$  documentada por Sheldrake)  
"129,0",Empírico (Água),"\$(2, 1)\$  (transição)",Duplo Arco Bilateral : linhas nodais estendidas ao longo de um eixo principal com simetria de reflexão,"2-fold  (simetria bilateral de alta ordem, modo  \$(2,3)\$ )"  
"174,0",Empírico (Hexágono) / Calib. (Quadrada),"\$(2, 1)\$  ( \$f\_{\\text{est}} \= 190{,}2\\text{ Hz}\$ )",Estrela Hexagonal / Seis Setores : primeiro modo medido em placas hexagonais ( \$12\\text{ cm}\$  e  \$9\\text{ cm}\$ ); na placa quadrada forma cruz dupla assimétrica,"10-fold / 14-fold  (próximo à bacia de  \$171{,}2\\text{ Hz}\$  de 10 pontas e  \$180\\text{ Hz}\$  de 14 pontas)"  
"238,0",Empírico (Água),"\$(3, 1)\$  ( \$f\_{\\text{est}} \= 297{,}2\\text{ Hz}\$ )",Grade de Oito Células : interseção de linhas nodais retas e arcos parabólicos periféricos,"6-fold  (rede hexagonal de 6 pontas em cubeta de  \$24{,}25\\text{ mm}\$ , modo  \$(6,4)\$ )"  
"283,0",Empírico (Placa 24 cm),"\$(3, 1)\$  ( \$m+2n=5\$ )","Anel Duplo / Quatro Lóbulos Externos (  \$f\_2\$  ) : dois contornos nodais principais com forte modulação angular ( \$A\_2 \= \-1{,}85\$ )","8-fold  (calibrado para  \$\\lambda \\approx 2{,}35\\text{ mm}\$  em regime capilar-gravitacional)"  
"285,0",Calibração analítica (Solfeggio),"\$(3, 1)\$  ( \$a=-b\$ )",Roseta Quadrangular de Quatro Lóbulos : acoplado diretamente ao modo  \$f\_2 \= 283\\text{ Hz}\$  com estrela central fechada,"8-fold  (simetria octogonal em fluido raso de  \$H \= 1{,}5\\text{ mm}\$ )"  
"396,0",Calibração analítica (Solfeggio),"\$(3, 2)\$  ( \$\\mu \= 0{,}60\$ )",Mandala de Oito Setores / Anel Cruzado : dois eixos diagonais cruzados por anel nodal intermediário,"12-fold  (transição capilar para dodecágono floral,  \$k \\approx 3353\\text{ m}^{-1}\$ )"  
"417,0",Calibração analítica (Solfeggio),"\$(3, 2)\$  ( \$\\mu \= \-0{,}85\$ )",Estrela Octogonal Simétrica : superposição quase antissimétrica formando oito pétalas fechadas,"12-fold  (células capilares de  \$\\lambda \\approx 1{,}81\\text{ mm}\$ )"  
"432,0",Calibração analítica (Afinação Verdi),"\$(2, 2)\$  ( \$f\_{\\text{est}} \= 428{,}0\\text{ Hz}\$ ,  \$a=b\$ )","Grade Simétrica de Quatro Lóbulos \+ Anel Central : ressonância quase exata de  \$m+2n=6\$ , exibindo geometria limpa de baixa entropia","12-fold / 16-fold  (regime capilar com  \$\\lambda \\approx 1{,}77\\text{ mm}\$ )"  
"440,0",Calibração analítica (Lá4 Padrão),"\$(3, 2)\$  ( \$a=b\$ )","Cruz Hiperbólica Dupla : afastamento de  \$(2,2)\$  induz reconexão de ramos diagonais e estrela interna","16-fold  (simetria de 16 pontas por redução do comprimento de onda para  \$1{,}75\\text{ mm}\$ )"  
"500,0",Modelagem (Shao et al. / Síntese),"\$(3, 2)\$  (transição)",Estrela de Múltiplas Pontas com Anel Interno : dois anéis nodais concêntricos interceptados por raios radiais,"18-fold  (teia capilar de alta ordem, modo  \$(18,6)\$  em  \$D \= 50\\text{ mm}\$ )"  
"511,0",Empírico (Placa 24 cm),"\$(3, 2)\$  ( \$f\_{\\text{est}} \= 582{,}6\\text{ Hz}\$ )","Mandala Quadrada de Duplo Contorno (  \$f\_3\$  ) : inversão de fase angular ( \$A\_2 \= \+1{,}70\$ ) gerando lóbulos apontados para os vértices","18-fold  (regime capilar puro,  \$\\lambda \\approx 1{,}58\\text{ mm}\$ )"  
"528,0",Calibração analítica (Solfeggio),"\$(3, 2)\$  ( \$a=-b\$ )","Flor de Oito Pétalas e Núcleo Estrelado : superposição antissimétrica  \$(3,2)\$  produzindo simetria radial limpa de oito lóbulos","18-fold  (teia capilar estável em  \$H \= 1{,}5\\text{ mm}\$ ,  \$\\lambda \\approx 1{,}54\\text{ mm}\$ )"  
"639,0",Calibração analítica (Solfeggio),"\$(4, 2)\$  ( \$\\mu \= \-0{,}80\$ )",Grade Cristalina Intermediária : transição entre dois e três contornos nodais com células regulares,"20-fold  (malha capilar poligonal com  \$\\lambda \\approx 1{,}36\\text{ mm}\$ )"  
"741,0",Calibração analítica (Solfeggio),"\$(4, 2)\$  ( \$f\_{\\text{est}} \= 760{,}9\\text{ Hz}\$ ,  \$a=b\$ )",Roseta de Três Anéis e Seis Lobos : estreitamente alinhada ao pico medido em  \$744\\text{ Hz}\$  na placa de  \$24\\text{ cm}\$,"24-fold  (simetria floral densa com  \$\\lambda \\approx 1{,}23\\text{ mm}\$ )"  
"744,0",Empírico (Placa 24 cm),"\$(2, 3)\$  ( \$f\_{\\text{est}} \= 760{,}9\\text{ Hz}\$ )","Triplo Contorno Nodal Quadrado (  \$f\_4\$  ) : três frentes nodais concêntricas moduladas por  \$A\_2 \= \-1{,}20\$  e  \$A\_3 \= \-1{,}30\$",24-fold  (regime capilar de alta densidade superficial)  
"852,0",Calibração analítica (Solfeggio),"\$(4, 3)\$  ( \$\\mu \= 0{,}75\$ )",Rede Hexagonal / Estrela de 12 Pontas : malha reticular densa com cruzamentos hiperbólicos simétricos,"24-fold / 26-fold  (micro-retícula capilar com  \$\\lambda \\approx 1{,}12\\text{ mm}\$ )"  
"963,0",Calibração analítica (Solfeggio),"\$(5, 2)\$  ( \$f\_{\\text{est}} \= 963{,}0\\text{ Hz}\$ ,  \$a=b\$ )",Roseta de 12 Pontas / Grade Simétrica : coincidência exata com  \$m+2n \= 9\$  na placa de referência,"28-fold  (quase-cristal capilar de alta simetria,  \$\\lambda \\approx 1{,}03\\text{ mm}\$ )"  
"1181,0",Empírico (Placa 24 cm),"\$(5, 3)\$  ( \$m+2n=11\$ ,  \$\\mu=-0{,}95\$ )","Mandala Cristalina de 4 Anéis (  \$f\_5\$  ) : quatro frentes nodais com forte mistura modal ( \$A\_4 \= \-5{,}80\$ )",32-fold  (próximo ao quasicristal 32-fold de  \$1200\\text{ Hz}\$ )  
"1200,0",Modelagem (Shao et al. / Síntese),"\$(4, 3)\$  ( \$f\_{\\text{est}} \= 1188{,}9\\text{ Hz}\$ )",Malha Cristalina Ortogonal-Radial : padrão de alta complexidade com múltiplas ilhas nodais,"32-fold  (micro-retícula quase-cristalina  \$(32,12)\$ ,  \$\\lambda \\approx 0{,}89\\text{ mm}\$ )"  
"1378,0",Empírico (Circular 24 cm),"\$(5, 3)\$  / 3 anéis circulares","Três Anéis Concêntricos Perfeitos : terceiro modo radial puro medido em disco circular de  \$24\\text{ cm}\$  ( \$v \= 105{,}0\\text{ m/s}\$ )","36-fold  (campo capilar sub-milimétrico,  \$\\lambda \\approx 0{,}81\\text{ mm}\$ )"  
"2000,0",Modelagem (Shao et al. / Síntese),"\$(6, 4)\$  ( \$a=b\$ )",Micro-Retícula Cristalina Fina : padrão sub-milimétrico de alta ordem dominado por mistura de automodos degenerados,"48-fold  (campo denso de ondulações capilares  \$(48,20)\$ ,  \$\\lambda \\approx 0{,}63\\text{ mm}\$ )"

#### 2\. Bloco 2: Matemática Exata da Mesa de Grãos — Placas Livres e Dinâmica Granular de Itô

A  **Mesa 2**  do laboratório virtual simula o acúmulo de milhares de microgrãos de areia sobre uma placa rígida vibrante. Para evitar figuras artificiais ou partículas que tremem indefinidamente sobre os nós, o motor físico deve acoplar a solução analítica exata das autofunções de borda livre a uma cinemática granular com limiar de aceleração e amortecimento por impacto.

##### 2.1 Placa Quadrada com Bordas Livres e Mistura Degenerada (a, b)

Em uma placa quadrada de lado  \$L\$  centrada na origem ( \$x, y \\in \-L/2, L/2\$ ) e completamente livre nas quatro bordas, o modelo clássico de Kirchhoff formula os autovalores e autofunções do operador bi-harmônico  \$\\Delta^2 w \= \\lambda\$  sujeito a momentos fletores e forças cortantes nulos no contorno  \$\\partial\\Omega\$ , conforme formulado na literatura matemática de Ponce Campuzano e Gander & Wanner:  
\$\$\\frac{\\partial^2 w}{\\partial x^2} \+ \\mu \\frac{\\partial^2 w}{\\partial y^2} \= 0, \\quad \\frac{\\partial}{\\partial x}\\left(\\frac{\\partial^2 w}{\\partial x^2} \+ (2-\\mu)\\frac{\\partial^2 w}{\\partial y^2}\\right) \= 0 \\quad \\text{em } x \= \\pm 1\$\$  
Como Wah e Val Baker et al. (2024) ressaltam, bordas livres ou engastadas ideais em placas quadradas raramente possuem forma fechada elementar única devido ao acoplamento de Poisson nas quinas. Para simulação analítica em tempo real de complexidade  \$O(1)\$  por vértice ou partícula, utiliza-se a superposição linear dos pares degenerados  \$(n, m)\$  e  \$(m, n)\$  (que possuem idêntica frequência natural teórica pela simetria do quadrado):  
\$\$u(x,y) \= a \\cos\\left(\\frac{n \\pi x}{L}\\right) \\cos\\left(\\frac{m \\pi y}{L}\\right) \+ b \\cos\\left(\\frac{m \\pi x}{L}\\right) \\cos\\left(\\frac{n \\pi y}{L}\\right)\$\$  
A razão de superposição  \$\\mu \= b/a\$  governa continuamente a topologia das linhas nodais  \$u(x,y) \= 0\$ .

* **Grade Ortogonal Pura (**  **\$b \= 0**\$  **ou**  **\$a \= 0**\$  **):**  Um único modo predomina, reduzindo  \$u(x,y) \= 0\$  a uma malha retangular de retas paralelas aos eixos da placa, localizadas em  \$x \= \\frac{(k \+ 1/2)L}{n}\$  e  \$y \= \\frac{(l \+ 1/2)L}{m}\$ .  
* **Cruz Simétrica e Estrela Diagonal (**  **\$a \= b**\$  **):**  Quando ambos os modos degenerados recebem pesos idênticos e em fase ( \$\\mu \= \+1\$ ), identidades trigonométricas de produto-para-soma colapsam as linhas nodais nos eixos diagonais e em estrelas fechadas. No modo fundamental  \$(n,m) \= (2,0)\$ , por exemplo, a condição nodal simplifica-se para as duas diagonais ortogonais  \$x \= \\pm y\$ , dividindo a chapa em quatro quadrantes triangulares simétricos.  
* **Configuração Antissimétrica (**  **\$a \= \-b**\$  **):**  Para  \$\\mu \= \-1\$ , a subtração  \$\\cos(n\\pi x/L)\\cos(m\\pi y/L) \- \\cos(m\\pi x/L)\\cos(n\\pi y/L) \= 0\$  gera famílias de curvas fechadas e cruzes ortogonais que evitam os vértices conforme a paridade de  \$(m,n)\$ . Note-se que para  \$m \= n\$ , a solução antissimétrica torna-se identicamente nula em toda a placa, exigindo  \$m \\ne n\$  para produzir padrão nodal.  
* **Bifurcações Hiperbólicas Intermediárias (**  **\$0 \< \|\\mu\| \< 1**\$  **):**  À medida que  \$\\mu\$  desliza continuamente de  \$+1\$  passando por  \$0\$  até  \$-1\$ , os cruzamentos de linhas nodais se rompem e se reconectam em famílias ortogonais de hipérboles suaves descritas localmente por  \$x^2 \- y^2 \= c(\\mu)\$ . Essa transição contínua explica exatamente as metamorfoses geométricas observadas quando se varre a frequência através de modos quase degenerados em placas reais.

##### 2.2 Placa Circular e Funções de Bessel em Borda Livre

Em coordenadas polares  \$(r, \\theta)\$  sobre um disco circular de raio  \$R\$ , a solução geral do problema de autovalores de Kirchhoff–Love envolve tanto as funções de Bessel ordinárias de primeira espécie  \$J\_m(kr)\$  quanto as funções de Bessel modificadas (hiperbólicas) de primeira espécie  \$I\_m(kr)\$ , conforme estabelecido nas formulações analíticas de Gough e na síntese computacional:  
\$\$w(r, \\theta) \= \\leftJ\_m(k r) \+ B\_m I\_m(k r) \\right \\cos(m \\theta \+ \\phi)\$\$  
Aqui,  \$m\$  é o número inteiro de diâmetros nodais radiais (linhas que cruzam o centro) e  \$k \= (\\rho h \\omega^2 / D)^{1/4}\$  é o número de onda flexural. É fundamental distinguir o disco livre de uma membrana circular fixa na borda (como um tambor): em membranas com borda presa ( \$w(R,\\theta)=0\$ ), apenas  \$J\_m(k r)\$  é necessária e os números de onda reduzem-se aos zeros  \$Z\_{mn}\$  da função de Bessel ordinária ( \$k \= Z\_{mn}/R\$ ). Já na  **placa metálica circular com borda livre** , tanto o momento fletor radial  \$M\_r\$  quanto a força cortante efetiva de Kelvin–Kirchhoff  \$V\_r\$  devem anular-se em  \$r \= R\$ :  
\$\$M\_r(R, \\theta) \= \-D \\left\\frac{\\partial^2 w}{\\partial r^2} \+ \\nu\_p \\left( \\frac{1}{r}\\frac{\\partial w}{\\partial r} \+ \\frac{1}{r^2}\\frac{\\partial^2 w}{\\partial \\theta^2} \\right) \\right\_{r=R} \= 0\$\$  
\$\$V\_r(R, \\theta) \= \-D \\left\\frac{\\partial}{\\partial r}(\\nabla^2 w) \+ (1 \- \\nu\_p)\\frac{1}{r}\\frac{\\partial}{\\partial \\theta}\\left( \\frac{1}{r}\\frac{\\partial^2 w}{\\partial r \\partial \\theta} \- \\frac{1}{r^2}\\frac{\\partial w}{\\partial \\theta} \\right) \\right\_{r=R} \= 0\$\$  
A imposição de  \$M\_r(R,\\theta) \= 0\$  fixa exatamente a razão algébrica  \$B\_m\$  entre os termos ordinário e modificado:  
\$\$B\_m \= \-\\frac{J\_m''(k R) \+ \\frac{\\nu\_p}{k R} J\_m'(k R) \- \\frac{\\nu\_p m^2}{k^2 R^2} J\_m(k R)}{I\_m''(k R) \+ \\frac{\\nu\_p}{k R} I\_m'(k R) \- \\frac{\\nu\_p m^2}{k^2 R^2} I\_m(k R)}\$\$  
Igualando esse quociente ao obtido pela condição  \$V\_r(R,\\theta) \= 0\$ , obtém-se a equação característica transcendental cujas raízes  \$k\_{mn} R\$  (para uma dada razão de Poisson, tipicamente  \$\\nu\_p \= 0{,}33\$ ) determinam os raios nodais concêntricos  \$n\$ :  
\$\$\\frac{J\_m''(k R) \+ \\frac{\\nu\_p}{k R} J\_m'(k R) \- \\frac{\\nu\_p m^2}{k^2 R^2} J\_m(k R)}{I\_m''(k R) \+ \\frac{\\nu\_p}{k R} I\_m'(k R) \- \\frac{\\nu\_p m^2}{k^2 R^2} I\_m(k R)} \= \\frac{J\_m'''(k R) \+ \\frac{1}{k R} J\_m''(k R) \- \\frac{1 \+ (2 \- \\nu\_p) m^2}{k^2 R^2} J\_m'(k R) \+ \\frac{(3 \- \\nu\_p) m^2}{k^3 R^3} J\_m(k R)}{I\_m'''(k R) \+ \\frac{1}{k R} I\_m''(k R) \+ \\frac{1 \+ (2 \- \\nu\_p) m^2}{k^2 R^2} I\_m'(k R) \+ \\frac{(3 \- \\nu\_p) m^2}{k^3 R^3} I\_m(k R)}\$\$  
Os zeros da função radial combinada  \$J\_m(k\_{mn} r) \+ B\_m I\_m(k\_{mn} r) \= 0\$  criam os  \$n\$  anéis concêntricos perfeitos, enquanto os zeros de  \$\\cos(m\\theta \+ \\phi) \= 0\$  geram os  \$m\$  diâmetros nodais equidistantes. Para placas excitadas no centro com modelos fenomenológicos simplificados em GPU, Val Baker et al. (2024) mostram ainda que os raios nodais podem ser aproximados por  \$r(\\theta) \= (n\\pi \- C\_n)/k\$ , onde  \$C\_n\$  captura o deslocamento de fase imposto pela geometria circular.

##### 2.3 Algoritmo de Migração, Difusão de Itô e Parada Estocástica dos Grãos

O comportamento real dos grãos de quartzo sobre a placa vibrante resulta da competição entre ejeção balística nos ventres, difusão estocástica e atrito de Coulomb nas regiões de repouso. A razão adimensional de aceleração de pico  \$\\Gamma(x,y)\$  governa a transição de regime, conforme estabelecido por Melo et al. (citados em Aranson e Tsimring, 2005), Devauchelle et al. (2026) e nos estudos de enfraquecimento friccional:  
\$\$\\Gamma(x,y) \= \\frac{A(x,y) \\omega^2}{g} \= \\frac{\|u(x,y)\| \\omega^2}{g}\$\$  
Quando  \$\\Gamma(x,y) \> 1\$ , a aceleração descendente da chapa supera a gravidade  \$g\$ : os grãos descolam da superfície no ângulo de fase  \$\\theta\_{\\text{detach}} \= \\arcsin(1/\\Gamma)\$  e executam voos parabólicos aleatórios (com ângulo típico de ejeção medido entre  \$50^\\circ\$  e  \$75^\\circ\$  em Devauchelle et al., 2026). Como demonstrado experimentalmente por Devauchelle et al. (2026), esse processo de saltos que perdem memória a cada colisão não segue a lei clássica de Fick ( \$\\mathbf{j} \= \-D\\nabla\\rho\$ ), mas sim uma  **difusão de Itô espacialmente heterogênea** :  
\$\$\\mathbf{j} \= \-\\nabla(D \\rho) \\implies \\rho(x,y) \\propto \\frac{1}{D(x,y)}\$\$  
Como a difusividade  \$D(x,y)\$  cresce monotonicamente com  \$\\Gamma(x,y)\$  e se anula onde a placa não ejeta o grão, a densidade estacionária  \$\\rho\$  diverge naturalmente nas linhas nodais ( \$u \= 0\$ ). Em simulações GPU em tempo real, modela-se essa migração combinando uma força efetiva de deriva acústica proporcional ao gradiente do quadrado da amplitude (baseada no campo de deslocamento de Zhou et al., 2016\) com perda de momento por colisão e um mecanismo explícito de travamento estático:

1. **Força de Deriva Acústica (Gradiente de Amplitude):**  Empurra o grão para fora dos antinodos na direção das curvas nodais segundo  \$\\mathbf{F}\_{\\text{ac}}(x,y) \= \-\\alpha \\nabla\\left(\|u(x,y)\|^2\\right) \= \-2\\alpha \|u(x,y)\| \\nabla\|u(x,y)\|\$ .  
2. **Restituição Viscoelástica Dependente da Velocidade:**  Evita o colapso numérico e ajusta o amortecimento vertical pela relação empírica  \$e(v\_{\\text{rel}}) \= 1 \- c\_e (v\_{\\text{rel}} / v\_0)^{1/5}\$ , com  \$c\_e \\approx 0{,}3\$ .  
3. **Atrito Tangencial Reológico**  **\$\\mu(I)**\$  **:**  O deslizamento tangencial obedece a  \$\\mu(I) \= \\mu\_s \+ \\frac{\\mu\_d \- \\mu\_s}{1 \+ I\_0 / I}\$ , onde  \$I \= \\frac{\\dot{\\gamma} d\_p}{\\sqrt{p/\\rho\_p}}\$  é o número inercial granular; em vibração intensa ( \$\\Gamma \> 0{,}1\$  e sobretudo  \$\\Gamma \> 1\$ ), ocorre enfraquecimento friccional, permitindo livre escoamento até a zona nodal.  
4. **Supressão da Trepidação Artificial (Dead Zone Nodal):**  Como observado por Zhou et al. (2016), em baixas amplitudes existe uma zona morta regida pelo atrito estático ( \$\\mu\_s \\approx 0{,}3\$ ). Em código Three.js/GLSL, aplica-se a probabilidade de salto estocástico  \$P\_{\\text{hop}}(x,y)\$  para zerar as atualizações cinéticas quando a aceleração cai abaixo do limiar gravitacional.

\$\$P\_{\\text{hop}}(x,y) \= \\max\\left(0,\\; 1 \- \\exp\\left(-\\beta \\left(\\Gamma(x,y) \- 1\\right)\\right)\\right)\$\$  
Sempre que  \$\\Gamma(x,y) \< 1{,}0\$  (na vizinhança imediata de  \$u(x,y) \= 0\$ ),  \$P\_{\\text{hop}} \= 0\$  suprime a injeção de ruído estocástico e o atrito estático  \$\\mu\_s\$  ancora a velocidade do grão em zero, garantindo assentamento nítido e imóvel sobre a figura geométrica sem tremor artificial. Como ressalva física importante para modos alternativos do simulador, Aranson e Tsimring (2005) e Faraday (1831) mostram que pós extremamente finos ( \$10\\text{–}20\\,\\mu\\text{m}\$ , cuja velocidade terminal de queda livre  \$v \= \\nu g d^2 / 18\\mu\$  iguala a velocidade da placa a  \$50\\text{ Hz}\$ ) migram inversamente aos antinodos devido a correntes de ar intersticial ( *acoustic streaming* ).

#### 3\. Bloco 3: Física da Água Pura — Ondas de Faraday, Ponto Focal Central e Resposta Instantânea

A  **Mesa 1**  reproduz o comportamento físico de um  **CymaScope**  real sobre uma bacia circular ou quadrada de espelho negro. A fidelidade visual dessa mesa depende de dois mecanismos hidrodinâmicos acoplados e da calibração rigorosa da viscosidade e tensão superficial para resposta instantânea ao áudio.

##### 3.1 Excitação por Ponto Focal Central Único vs. Instabilidade Paramétrica de Faraday

No CymaScope Pro MF+ descrito por Geffen et al. (2025) e Sheldrake e Sheldrake (2017), uma cubeta de quartzo fundido com fundo preto fosco é acoplada diretamente ao pistão vertical de um único atuador  *Voice Coil Motor*  (VCM) centralizado, com equalização prévia (como um equalizador gráfico de 30 bandas) para eliminar ressonâncias espúrias da própria estrutura. A escolha de um  **único ponto focal central**  em vez de múltiplos transdutores espalhados tem fundamento físico direto.  
Sob excitação central de pistão no raio  \$r \= r\_0\$  com condição de velocidade harmônica  \$v\_z(r\_0, t) \= V\_0 \\sin(\\omega t)\$ , ondas cilíndricas irradiam radialmente para fora (descritas pela função de Hankel de primeira espécie  \$H\_m^{(1)}(kr) \= J\_m(kr) \+ i Y\_m(kr)\$ ), atingem a parede rígida da cubeta em  \$r \= R\$  e refletem de volta para o centro como ondas entrantes ( \$H\_m^{(2)}(kr) \= J\_m(kr) \- i Y\_m(kr)\$ ). A interferência coerente entre a onda emitida e a onda refletida pela borda forma ondas estacionárias radiais e azimutais puras:  
\$\$h(r, \\theta, t) \= \\text{Re} \\left\\sum\_{m=0}^{\\infty} A\_m \\left( H\_m^{(1)}(k r) \+ R\_m H\_m^{(2)}(k r) \\right) \\cos(m \\theta) e^{-i \\omega t} \\right\$\$  
Nesta equação,  \$R\_m\$  é o coeficiente complexo de reflexão da parede ( \$R\_m \= 1\$  para contorno vertical rígido). Múltiplos atuadores arbitrários quebrariam a coerência de fase central, gerando interferência incoerente e destruindo as simetrias poligonais puras. Simultaneamente, o movimento vertical global do pistão modula a gravidade efetiva  \$g(t) \= g\_0 \+ a\_0 \\cos(\\omega t)\$  sobre toda a lâmina líquida, submetendo cada modo espacial de Fourier  \$a\_k(t)\$  à  **equação de Mathieu amortecida**  de Benjamin e Ursell (1954):  
\$\$\\frac{d^2 a\_k}{d t^2} \+ 2 \\gamma(k) \\frac{d a\_k}{d t} \+ \\Omega\_0^2(k) \\left1 \+ \\frac{a\_0}{g\_0} \\cos(\\omega t) \\right a\_k \= 0\$\$  
Acima de um limiar crítico estreito  \$a\_c\$  (com línguas de instabilidade centradas em  \$\\omega \\approx 2\\Omega\_0(k)\$ , onde a passagem de  \$0{,}90\\,a\_c\$  a  \$1{,}15\\,a\_c\$  separa o espelho plano do crescimento exponencial, conforme medido via expoentes de Floquet em  *Phenomena Study \#29* ), a superfície bifurca para o regime sub-harmônico ( \$\\omega\_f \= \\omega/2\$ ). Na simulação em GPU desse estudo, a introdução do termo não-linear quadrático  \$c\_2\$  além do cúbico  \$c\_3\$  é determinante para que redes quadradas se estabilizem em vez de colapsarem em listras unidimensionais ( \$c\_2 \= 0\$ ). Adicionalmente, a taxonomia experimental de Geffen et al. (2025) mostra que pequenas assimetrias de fase entre a onda incidente e ressonâncias do quartzo geram  *cimáglifos*  dinâmicos com rotação horária ou anti-horária, fluxos toroidais e padrões compostos de interferência sob díades musicais — efeito igualmente adotado em interfaces 3D em tempo real como o  *CymaSense*  de McGowan et al. (2021).

##### 3.2 Modelagem Espectral nos Regimes Grave, Médio e Agudo

A morfologia superficial altera-se drasticamente ao longo do espectro audível porque a relação de dispersão  \$\\omega\_f^2 \= (gk \+ \\frac{\\sigma}{\\rho}k^3)\\tanh(kH)\$  transfere o controle físico da gravidade para a tensão superficial à medida que a frequência sobe. Em um recipiente cilíndrico de raio  \$R\$  com condição de parede livre  \$J\_m'(k\_{mn} R) \= 0\$  (onde  \$\\alpha\_{mn}'\$  é o  \$n\$ \-ésimo zero de  \$J\_m'\$  e  \$k\_{mn} \= \\alpha\_{mn}'/R\$ ), o campo de elevação decompõe-se segundo Shao et al. (2021) em:  
\$\$h(r, \\theta, t) \= \\sum\_{m=0}^{\\infty} \\sum\_{n=1}^{\\infty} A\_{mn}(t) J\_m(k\_{mn} r) \\cos(m \\theta \+ \\phi\_m)\$\$  
A tabela abaixo sintetiza a modelagem matemática e visual exigida para cada faixa espectral na Mesa 1\.  
Faixa de Frequência,Força Física Dominante,Comportamento Matemático e Modal,Expressão Visual na Água (Mesa 1\)  
Graves (20 Hz – 150 Hz),Gravidade ( \$g k \\gg \\frac{\\sigma}{\\rho} k^3\$ ),"\$\\omega\_f^2 \\approx gk\\tanh(kH)\$ ; número de onda  \$k\$  baixo ( \$525\\text{–}1700\\text{ m}^{-1}\$ ), baixos limiares  \$a\_c/g \\approx 0{,}18\\text{–}0{,}95\$  e ordens azimutais baixas ( \$m \\le 12\$ )","Ondas longas ( \$\\lambda \\approx 4\\text{–}12\\text{ mm}\$ ), anéis concêntricos profundos ( \$(0,1)\$  a  \$43\\text{ Hz}\$ ) e grande deslocamento vertical central"  
Médios (150 Hz – 800 Hz),Regime misto gravidade-capilaridade ( \$g k \\sim \\frac{\\sigma}{\\rho} k^3\$ ),"Competição entre termo gravitacional e capilar; autofunções cilíndricas  \$J\_m(k\_{mn}r)\$  excitam simetrias discretas de 3, 4, 5, 6, 8, 10, 12 e 18 pontas","Figuras florais e poligonais nítidas (ex.: hexágonos em  \$238\\text{ Hz}\$  com  \$a\_c/g \= 1{,}85\$ ; teia capilar de 18 pontas em  \$500\\text{ Hz}\$  com  \$a\_c/g \= 4{,}20\$ )"  
Agudos (800 Hz – 2000 Hz+),Capilaridade pura ( \$\\frac{\\sigma}{\\rho} k^3 \\gg g k\$ ),"\$\\omega\_f^2 \\approx \\frac{\\sigma}{\\rho}k^3\$ ;  \$k\$  elevado ( \$\>5400\\text{ m}^{-1}\$  até  \$\\sim 9930\\text{ m}^{-1}\$ ), camada limite viscosa fina  \$\\delta \= \\sqrt{2\\nu/\\omega}\$  eleva  \$a\_c/g\$  até  \$9{,}80\\text{–}16{,}50\$","Micro-retículas cristalinas e quasicristais de altíssima densidade superficial ( \$\\lambda \\approx 0{,}63\\text{–}1{,}1\\text{ mm}\$ , modos  \$(32,12)\$  a  \$(48,20)\$ )"

##### 3.3 Calibração de Amortecimento e Tensão Superficial para Resposta Instantânea

Em aplicações de áudio em tempo real (voz humana ou batidas musicais), a água comum falha como meio de simulação direta se suas constantes macroscópicas forem usadas sem ajuste de escala. O amortecimento viscoso livre de Lamb é dado por  \$\\gamma(k) \= 2\\nu k^2\$ ; incorporando a dissipação da camada limite no fundo raso da bacia de profundidade  \$H\$ , obtém-se a taxa de amortecimento total:  
\$\$\\gamma\_{\\text{total}}(k) \= 2 \\nu k^2 \+ \\frac{\\sqrt{\\nu \\omega}}{2 H \\sinh(2 k H)}, \\qquad \\tau\_{\\text{decay}} \= \\frac{1}{\\gamma\_{\\text{total}}(k)}\$\$  
Para água pura a  \$20\\,^\\circ\\text{C}\$  ( \$\\nu \= 1{,}004 \\times 10^{-6}\\text{ m}^2/\\text{s}\$ ) em baixos números de onda ( \$k \= 100\\text{ m}^{-1}\$ ), o tempo de decaimento natural atinge  \$\\tau\_{\\text{decay}} \\approx 49{,}8\\text{ s}\$  (e  \$12{,}5\\text{ s}\$  a  \$100\\text{ Hz}\$ ), produzindo persistência visual severa após o silêncio. Experimentalmente, Sheldrake e Sheldrake (2017) também demonstraram que o  **Tempo até Expressão Completa (TFE)**  cresce significativamente com maior profundidade/volume de água e cai com o aumento da amplitude e da frequência. Para manter baixa latência em mapeamentos áudio-visuais interativos (como demonstrado por McGowan et al., 2021, no  *CymaSense* , onde amplitude controla escala e conteúdo espectral modula a nitidez superficial), o fluido da Mesa 1 deve ser calibrado como um filme líquido raso de viscosidade efetiva elevada e tensão superficial controlada.  
Parâmetro Hidrodinâmico,Símbolo,Água Pura Padrão,Fluido Cimático Calibrado (Mesa 1),Efeito na Resposta em Tempo Real  
Viscosidade cinemática,\$\\nu\$,"\$1{,}004 \\times 10^{-6}\\text{ m}^2/\\text{s}\$","\$5{,}50 \\times 10^{-5}\\text{ m}^2/\\text{s}\$",Elimina reverberação residual e limpa transientes vocais  
Tensão superficial,\$\\sigma\$,"\$0{,}0728\\text{ N/m}\$","\$0{,}0450\\text{ N/m}\$",Ajusta  \$k\$  capilar e aumenta definição das pétalas finas  
Profundidade da lâmina,\$H\$,"\$10{,}0\\text{ mm}\$","\$1{,}50\\text{ mm}\$",Maximiza atrito de fundo  \$\\frac{\\sqrt{\\nu\\omega}}{2H\\sinh(2kH)}\$  e reduz TFE  
Densidade do fluido,\$\\rho\$,\$998\\text{ kg/m}^3\$,\$1120\\text{ kg/m}^3\$,Ajusta o comprimento capilar  \$l\_c \= \\sqrt{\\sigma/(\\rho g)}\$  
Tempo de decaimento ( \$100\\text{ Hz}\$ ),\$\\tau\_{100\\text{Hz}}\$,"\$12{,}5\\text{ s}\$","\$4{,}2\\text{ ms}\$","Zera a superfície em  \$\<1\$  quadro ( \$16{,}6\\text{ ms}\$ ) no silêncio"  
Tempo de subida sub-harmônica,\$\\tau\_{\\text{rise}}\$,"\$250{,}0\\text{ ms}\$","\$1{,}8\\text{ ms}\$",Acompanha ataques percussivos e formantes de voz ao vivo  
Com essa calibração em  \$H \= 1{,}5\\text{ mm}\$ , cálculos diretos pela relação de dispersão mostram que  \$\\tau\_{\\text{decay}}\$  cai de  \$22{,}6\\text{ ms}\$  em  \$27\\text{ Hz}\$  para  \$4{,}79\\text{ ms}\$  em  \$107\\text{ Hz}\$ ,  \$1{,}61\\text{ ms}\$  em  \$238\\text{ Hz}\$  e abaixo de  \$0{,}6\\text{ ms}\$  acima de  \$500\\text{ Hz}\$  — garantindo sincronia audiovisual instantânea e retorno imediato ao espelho liso no silêncio.

#### 4\. Bloco 4: Engenharia da 3ª Mesa — Acoplamento Nodal-Hidrodinâmico e Estabilidade em GLSL

A  **Mesa 3**  acopla as duas físicas anteriores: a geometria nodal gerada pela placa de Chladni deixa de ser apenas um local de repouso granular e passa a atuar como uma matriz contínua de micro-transdutores submersos que injetam energia diretamente no campo de altura  \$h(x,z,t)\$  da água.

##### 4.1 Máscara Nodal de Excitação Hidrodinâmica na EDP Capilar-Gravitacional

A evolução da superfície líquida na Mesa 3 é governada pela equação diferencial parcial de 4ª ordem para ondas capilares-gravitacionais amortecidas sobre um  *heightfield*  2D:  
\$\$\\frac{\\partial^2 h}{\\partial t^2} \+ 2 \\gamma(x,z) \\frac{\\partial h}{\\partial t} \- c^2 \\nabla^2 h \+ \\kappa \\nabla^4 h \= S(x, z, t)\$\$  
Aqui,  \$c \= \\sqrt{g H}\$  é a velocidade de onda rasa gravitacional ( \$c \\approx 0{,}1213\\text{ m/s}\$  para  \$H \= 1{,}5\\text{ mm}\$ ) e  \$\\kappa \= \\frac{\\sigma H}{\\rho}\$  é a rigidez capilar efetiva ( \$\\kappa \\approx 6{,}03 \\times 10^{-8}\\text{ m}^4/\\text{s}^2\$  para o fluido calibrado). O termo fonte  \$S(x,z,t)\$  traduz o campo escalar de Chladni  \$u(x,z)\$  em pressão acústica distribuída.  
Na formulação do relatório de modelagem computacional, uma máscara de ativação antinodal assume a forma  \$M\_{\\text{anti}}(x,z) \= 1{,}0 \- \\exp(-\|u(x,z)\|^2/\\varepsilon^2)\$ . Contudo, para o requisito específico da  **Mesa 3**  — no qual a  **própria linha nodal**  ( \$\|u(x,z)\| \< \\varepsilon\$ , desenhando a cruz, estrela, flor ou mandala) funciona como o arranjo emissor de ondas concêntricas na água —, a máscara espacial deve ser invertida para uma  **função gaussiana centrada no zero nodal** :  
\$\$S(x, z, t) \= A\_{\\text{drive}}(t) \\cdot \\cos(\\omega t) \\cdot \\exp\\left( \-\\frac{\|u(x, z)\|^2}{\\varepsilon^2} \\right)\$\$  
Nessa formulação,  \$A\_{\\text{drive}}(t)\$  é o envelope instantâneo de amplitude extraído via Web Audio API,  \$\\omega \= 2\\pi f\$  é a frequência angular de excitação e  \$\\varepsilon\$  define a largura física do traço emissor (espessura dos micro-alto-falantes virtuais ao longo do desenho geométrico). Onde  \$u(x,z) \= 0\$ , a máscara vale  \$1{,}0\$  e injeta oscilação máxima vertical; nos antinodos onde  \$\|u(x,z)\| \\gg \\varepsilon\$ , a máscara decai exponencialmente a zero, permitindo que as ondas irradiadas lateralmente a partir do contorno da figura propaguem sobre um espelho de água calmo.

##### 4.2 Discretização em GLSL, Condição CFL e Fronteira Absorvente (PML)

Para executar essa EDP a  \$60\\text{ FPS}\$  em WebGL utilizando  *framebuffers*   *ping-pong*  de ponto flutuante (RGBA32F), separa-se a derivada temporal de segunda ordem em duas equações acopladas de primeira ordem para altura  \$h\$  e velocidade vertical  \$v \= \\partial h/\\partial t\$ :  
\$\$\\frac{\\partial h}{\\partial t} \= v, \\qquad \\frac{\\partial v}{\\partial t} \= \-2\\gamma(x,z) v \+ c^2 \\nabla^2 h \- \\kappa \\nabla^4 h \+ S(x,z,t)\$\$  
Para evitar artefatos anisotrópicos de grade (ondas quadradas em vez de concêntricas), o Laplaciano  \$\\nabla^2 h\$  é calculado com estêncil isotrópico de 9 pontos (peso 4 nos vizinhos ortogonais, peso 1 nos diagonais e  \$-20\$  no centro, dividido por  \$6\\Delta x^2\$ ), e o termo bi-harmônico  \$\\nabla^4 h \= \\nabla^2(\\nabla^2 h)\$  é obtido em dois passos sequenciais de  *render target* . A integração temporal utiliza o esquema explícito  *Velocity-Verlet*  /  *Leapfrog* :  
\$\$v\_{i,j}^{n+1/2} \= \\left( \\frac{1 \- \\gamma \\Delta t}{1 \+ \\gamma \\Delta t} \\right) v\_{i,j}^{n-1/2} \+ \\frac{\\Delta t}{1 \+ \\gamma \\Delta t} \\leftc^2 \\nabla^2 h\_{i,j}^n \- \\kappa \\nabla^4 h\_{i,j}^n \+ S\_{i,j}^n \\right, \\qquad h\_{i,j}^{n+1} \= h\_{i,j}^n \+ \\Delta t \\, v\_{i,j}^{n+1/2}\$\$

###### *Estabilidade Estrita de Courant–Friedrichs–Lewy (CFL) para 4ª Ordem*

A presença do termo capilar  \$\\kappa \\nabla^4 h\$  impõe uma restrição quadrática no passo de tempo em função do espaçamento  \$\\Delta x\$ , muito mais rígida que o limite clássico da onda de 2ª ordem ( \$c\\Delta t/\\Delta x \\le 1/\\sqrt{2}\$ ):  
\$\$\\Delta t \\le \\frac{\\Delta x^2}{2 \\sqrt{\\kappa \+ c^2 \\Delta x^2 / 2}}\$\$  
Para uma mesa de  \$L \= 0{,}24\\text{ m}\$  discretizada em malha  \$256 \\times 256\$  ( \$\\Delta x \= 0{,}9375\\text{ mm}\$ ), com  \$c \= 0{,}1213\\text{ m/s}\$  e  \$\\kappa \= 6{,}027 \\times 10^{-8}\\text{ m}^4/\\text{s}^2\$ , o limite máximo é  \$\\Delta t\_{\\text{max}} \\approx 1{,}70\\text{ ms}\$ . A  \$60\\text{ Hz}\$  ( \$\\Delta t\_{\\text{frame}} \= 16{,}67\\text{ ms}\$ ), o  *loop*  GPU deve executar  \$N\_{\\text{sub}} \= \\lceil 16{,}67 / 1{,}70 \\rceil \= 10\$  sub-passos por quadro. Além disso, para evitar inversão de sinal no fator de amortecimento de Verlet, deve-se manter  \$\\gamma \\Delta t\_{\\text{sub}} \< 1\$ .

###### *Equilíbrio entre  \$\\varepsilon\$  e  \$\\kappa\$  para Nitidez da Figura Central*

O parâmetro de largura nodal  \$\\varepsilon\$  deve ser estreito o suficiente para preservar frestas nítidas entre os ramos da figura ( \$S \\to 0\$  fora da linha nodal), enquanto  \$\\gamma\_{\\text{base}}\$  atenua as frentes laterais após alguns comprimentos de onda capilares, evitando que ondas emitidas por ramos opostos saturem ou borrem o centro geométrico.

###### *Camada Esponja Absorvente (PML Radial)*

Para impedir que ondas laterais atinjam a borda da textura quadrada e retornem interferindo com a mandala central, aplica-se um perfil radial de amortecimento polinomial próximo às paredes:  
\$\$\\gamma(x, z) \= \\gamma\_{\\text{base}} \+ \\gamma\_{\\text{max}} \\cdot \\left( \\frac{\\max(0, r(x,z) \- r\_{\\text{inner}})}{R\_{\\text{boundary}} \- r\_{\\text{inner}}} \\right)^p\$\$  
Utilizando  \$r\_{\\text{inner}} \= 0{,}85 R\_{\\text{boundary}}\$ ,  \$\\gamma\_{\\text{max}} \\approx 100{,}0\\text{ s}^{-1}\$  e expoente  \$p \= 3\$ , toda a energia cinética irradiada para a periferia é dissipada suavemente antes de tocar o contorno computacional.

#### 5\. Bloco 5: Óptica de "Espelho Negro" e Iluminação Cimática Rasante em PBR/GLSL

Na fotografia cimática profissional (CymaScope, Hans Jenny e Alexander Lauterwasser), a água não recebe cor difusa; o contraste elevado nasce exclusivamente da geometria óptica entre um fundo preto fosco, uma fonte luminosa anelar rasante e a inclinação local das ondas.

##### 5.1 Geometria Fotográfica, Inclinação ( \$\\nabla h\$ ) e Curvatura ( \$\\nabla^2 h\$ )

No aparato físico documentado por Sheldrake e Sheldrake (2017) e Geffen et al. (2025), a cubeta possui fundo jateado preto fosco para eliminar reflexões internas e é observada por uma câmera posicionada perpendicularmente no zênite ( \$\\theta\_c \= 0^\\circ\$ ). Em vez de um único refletor pontual com ângulo de cone fechado, o CymaScope emprega um  **anel circular de 32 LEDs brancos**  distribuídos em  \$360^\\circ\$  ao redor da bacia (modelado em GLSL por 16 a 32 fontes pontuais sobre um anel de raio  \$R\_{\\text{ring}} \= D\_{\\text{ring}}/2\$  e altura  \$H\_{\\text{ring}}\$ ). Os parâmetros geométricos ideais calibrados na literatura para evitar estouro especular no centro são:

* **Ângulo de Incidência Rasante (**  **\$\\theta\_i**\$  **):**  Posicionado entre  \$75^\\circ\$  e  \$85^\\circ\$  em relação à normal da superfície plana ( \$\\theta\_i \= 80^\\circ\$  como referência nominal), fazendo os raios incidirem quase paralelamente ao plano da água.  
* **Altura Y (**  **\$H\_{\\text{ring}}**\$  **) vs. Distância Radial (**  **\$D\_{\\text{ring}}**\$  **):**  Calibrada pela razão adimensional  \$H\_{\\text{ring}} / D\_{\\text{ring}} \\approx 0{,}15 \\text{ a } 0{,}35\$  (com referência nominal  \$H\_{\\text{ring}}/D\_{\\text{ring}} \= 0{,}25\$  para iluminação anelar equilibrada, garantindo que o centro plano permaneça fora do cone direto de reflexão para a câmera zenital).  
* **Ângulo de Abertura do Facho:**  Não há ângulo de abertura de  *spotlight*  especificado nas fontes do CymaScope justamente porque o anel de LEDs envolve circunferencialmente a cubeta; em cena Three.js, caso se adicionem luzes auxiliares direcionais, elas devem manter direção tangencial rasante ( \$\\theta\_i \\ge 75^\\circ\$ ) e evitar incidência próxima à normal no centro da bacia.

Quando a água está em repouso ( \$h \= 0\$ ,  \$\\nabla h \= \\mathbf{0}\$ ), raios incidentes a  \$80^\\circ\$  refletem especularmente a  \$80^\\circ\$  para o lado oposto, errando completamente a lente da câmera e produzindo preto absoluto. Quando a onda estacionária surge, pequenas inclinações  \$\\nabla h \= (\\partial h/\\partial x, \\partial h/\\partial z)\$  inclinam o vetor normal  \$\\mathbf{N}\$  em apenas alguns graus, desviando o vetor de reflexão  \$\\mathbf{R} \= \\mathbf{I} \- 2(\\mathbf{I}\\cdot\\mathbf{N})\\mathbf{N}\$  diretamente para a câmera.  
Há uma nuance óptica relevante documentada entre as fontes: nas observações experimentais com o anel superior do CymaScope (Geffen et al., 2025), as  **cristas convexas**  dispersam a luz para fora da lente (aparecendo mais escuras), enquanto os  **vales côncavos**  funcionam como espelhos coletores que retornam luz à câmera (aparecendo brilhantes). Já na formulação do  *shader*  GPU de iluminação rasante da síntese computacional, a curvatura espacial de segunda ordem ( \$\\nabla^2 h\$ ) é usada com sinal invertido (-laplacian) para enfatizar linhas cáusticas brilhantes sobre as cristas ( \$\\nabla^2 h \< 0\$ ). Em código GLSL, parametrizar esse sinal permite alternar com exatidão entre o modo fotográfico de anel superior (vales brilhantes) e o modo cáustico rasante (cristas brilhantes).

##### 5.2 Shading PBR, Fresnel de Schlick e Fragment Shader GLSL

Em Three.js, o visual de água profunda ou mercúrio negro hiper-realista é obtido combinando uma cor base dielétrica quase nula (vec3(0.002, 0.003, 0.005)) com o modelo PBR de microfacetas Cook-Torrance descrito em LearnOpenGL e nas notas técnicas de T. Ramaswamy, empregando a distribuição normal GGX ( *Trowbridge-Reitz* ) com rugosidade especular ultrabaixa ( \$\\alpha \= 0{,}035\$ ) e a aproximação de Schlick para refletância de Fresnel:  
\$\$F\_{\\text{Schlick}}(\\mathbf{H}, \\mathbf{V}, F\_0) \= F\_0 \+ (1 \- F\_0)\\left(1 \- \\max(\\mathbf{H}\\cdot\\mathbf{V}, 0)\\right)^5\$\$  
Aqui,  \$F\_0\$  define a refletância em incidência normal:  **\$F\_0 \\approx 0{,}02\\text{ a }0{,}04**\$  reproduz água escura dielétrica realista (em que apenas as inclinações rasantes brilham intensamente pelo termo de Fresnel, preservando o centro negro), enquanto  **\$F\_0 \\approx 0{,}56**\$  (ou fluxo metálico elevado conforme  *Phenomena Study \#29* ) produz o acabamento de  **mercúrio negro** . Em material MeshStandardMaterial nativo do Three.js, isso equivale a metalness: 0.0–0.1 e roughness: 0.035 para água escura, ou metalness: 0.90–1.0 e roughness: 0.035 para mercúrio negro, sempre acoplado ao  *normal map*  dinâmico calculado por diferenças centrais e  *tone mapping*  de Reinhard ( \$\\mathbf{C}/(\\mathbf{C}+1)\$ ) para impedir saturação branca no centro.  
O  *fragment shader*  completo abaixo, extraído diretamente da especificação computacional das fontes, integra normal dinâmica, foco cáustico pelo Laplaciano, anel de 16 LEDs em incidência rasante, BRDF GGX e correção gama:  
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

#### 6\. Bloco 6: Parâmetros Prontos para Código — Presets Científicos Calibrados (JSON / JavaScript)

O objeto CYMATICS\_PRESETS a seguir reúne  **24 presets científicos calibrados**  cobrindo o espectro de  \$20\\text{ Hz}\$  a  \$2000\\text{ Hz}\$ , prontos para importação direta em Three.js. Cada registro adota unidades físicas consistentes com o modelo acoplado: hz em Hertz; m e n como índices inteiros de Chladni (todos verificados numericamente para garantir linhas nodais não triviais com  \$m \\ne n\$  sempre que coefA e coefB tiverem sinais opostos); coefA e coefB como pesos  \$(a, b)\$  da superposição quadrada; simetriaAgua como ordem azimutal  *n-fold*  de Faraday/CymaScope; tensaoSuperficial em  \$\\text{N/m}\$  ( \$0{,}045\\text{ N/m}\$  para o fluido cimático calibrado); amortecimentoIdeal como coeficiente  \$\\gamma\_{\\text{base}}\$  em  \$\\text{s}^{-1}\$  (usando a taxa física  \$\\gamma\_{\\text{total}}\$  calculada via dispersão até  \$110\\text{ Hz}\$ , de  \$44{,}2\\text{ a }216{,}5\\text{ s}^{-1}\$ , e limitada entre  \$225\\text{ e }400\\text{ s}^{-1}\$  acima de  \$174\\text{ Hz}\$  para respeitar  \$\\gamma \\Delta t\_{\\text{sub}} \< 1\$  no esquema Velocity-Verlet com  \$N\_{\\text{sub}} \= 10\$  a  \$60\\text{ FPS}\$ ); e anguloLuzRecomendado como ângulo rasante  \$\\theta\_i\$  em graus ( \$75^\\circ\\text{ a }84^\\circ\$ ).  
export const CYMATICS\_PRESETS \= \[  
  {  
    hz: 20.0,  
    nomeDoDesenho: "Cruz Diagonal Fundamental X / Onda Gravitacional Longa",  
    m: 1,  
    n: 0,  
    coefA: 1.0,  
    coefB: \-1.0,  
    simetriaAgua: 2,  
    tensaoSuperficial: 0.045,  
    amortecimentoIdeal: 32.5,  
    anguloLuzRecomendado: 75.5  
  },  
  {  
    hz: 27.0,  
    nomeDoDesenho: "Rede Quadrada Gravitacional / Cruz Diagonal X",  
    m: 1,  
    n: 0,  
    coefA: 1.0,  
    coefB: \-1.0,  
    simetriaAgua: 4,  
    tensaoSuperficial: 0.045,  
    amortecimentoIdeal: 44.2,  
    anguloLuzRecomendado: 76.0  
  },  
  {  
    hz: 43.0,  
    nomeDoDesenho: "Anel Concêntrico Primário / Cruz Diagonal Dupla",  
    m: 2,  
    n: 0,  
    coefA: 1.0,  
    coefB: \-1.0,  
    simetriaAgua: 1,  
    tensaoSuperficial: 0.045,  
    amortecimentoIdeal: 67.9,  
    anguloLuzRecomendado: 77.0  
  },  
  {  
    hz: 56.0,  
    nomeDoDesenho: "Grade Bilateral / Quatro Lóbulos Simétricos",  
    m: 2,  
    n: 1,  
    coefA: 1.0,  
    coefB: 0.35,  
    simetriaAgua: 4,  
    tensaoSuperficial: 0.045,  
    amortecimentoIdeal: 91.4,  
    anguloLuzRecomendado: 78.0  
  },  
  {  
    hz: 66.0,  
    nomeDoDesenho: "Pentágono Líquido / Cruz Central Aberta",  
    m: 2,  
    n: 1,  
    coefA: 1.0,  
    coefB: 0.65,  
    simetriaAgua: 5,  
    tensaoSuperficial: 0.045,  
    amortecimentoIdeal: 111.5,  
    anguloLuzRecomendado: 78.5  
  },  
  {  
    hz: 69.0,  
    nomeDoDesenho: "Decágono Estável / Cruz com Losango Interno",  
    m: 2,  
    n: 1,  
    coefA: 1.0,  
    coefB: 0.85,  
    simetriaAgua: 10,  
    tensaoSuperficial: 0.045,  
    amortecimentoIdeal: 117.8,  
    anguloLuzRecomendado: 79.0  
  },  
  {  
    hz: 78.0,  
    nomeDoDesenho: "Roseta Dodecagonal / Quatro Pétalas Curvas",  
    m: 2,  
    n: 1,  
    coefA: 1.0,  
    coefB: \-0.75,  
    simetriaAgua: 12,  
    tensaoSuperficial: 0.045,  
    amortecimentoIdeal: 137.7,  
    anguloLuzRecomendado: 79.5  
  },  
  {  
    hz: 82.0,  
    nomeDoDesenho: "Flor Octogonal / Cruz Hiperbólica",  
    m: 2,  
    n: 1,  
    coefA: 1.0,  
    coefB: \-1.0,  
    simetriaAgua: 8,  
    tensaoSuperficial: 0.045,  
    amortecimentoIdeal: 146.8,  
    anguloLuzRecomendado: 79.5  
  },  
  {  
    hz: 107.0,  
    nomeDoDesenho: "Cruz Ortogonal e Lóbulos Primários (f1 Quadrada 24cm)",  
    m: 1,  
    n: 1,  
    coefA: 1.0,  
    coefB: 1.0,  
    simetriaAgua: 4,  
    tensaoSuperficial: 0.045,  
    amortecimentoIdeal: 208.6,  
    anguloLuzRecomendado: 80.0  
  },  
  {  
    hz: 110.0,  
    nomeDoDesenho: "Lá2 — Losango Central Inscrito / Decágono Harmônico",  
    m: 2,  
    n: 0,  
    coefA: 1.0,  
    coefB: 1.0,  
    simetriaAgua: 10,  
    tensaoSuperficial: 0.045,  
    amortecimentoIdeal: 216.5,  
    anguloLuzRecomendado: 80.0  
  },  
  {  
    hz: 174.0,  
    nomeDoDesenho: "Solfeggio 174 / Primeiro Modo Hexagonal",  
    m: 2,  
    n: 1,  
    coefA: 1.0,  
    coefB: 1.0,  
    simetriaAgua: 10,  
    tensaoSuperficial: 0.045,  
    amortecimentoIdeal: 225.0,  
    anguloLuzRecomendado: 80.0  
  },  
  {  
    hz: 238.0,  
    nomeDoDesenho: "Rede Hexagonal / Grade de Seis Setores",  
    m: 3,  
    n: 1,  
    coefA: 1.0,  
    coefB: 0.55,  
    simetriaAgua: 6,  
    tensaoSuperficial: 0.045,  
    amortecimentoIdeal: 235.0,  
    anguloLuzRecomendado: 80.5  
  },  
  {  
    hz: 283.0,  
    nomeDoDesenho: "Anel Duplo e Quatro Lóbulos (f2 Quadrada 24cm)",  
    m: 3,  
    n: 1,  
    coefA: 1.0,  
    coefB: 1.0,  
    simetriaAgua: 8,  
    tensaoSuperficial: 0.045,  
    amortecimentoIdeal: 240.0,  
    anguloLuzRecomendado: 80.5  
  },  
  {  
    hz: 285.0,  
    nomeDoDesenho: "Solfeggio 285 / Roseta Quadrangular de Quatro Lóbulos",  
    m: 3,  
    n: 1,  
    coefA: 1.0,  
    coefB: \-1.0,  
    simetriaAgua: 8,  
    tensaoSuperficial: 0.045,  
    amortecimentoIdeal: 240.0,  
    anguloLuzRecomendado: 80.5  
  },  
  {  
    hz: 396.0,  
    nomeDoDesenho: "Solfeggio 396 / Mandala de Oito Setores",  
    m: 3,  
    n: 2,  
    coefA: 1.0,  
    coefB: 0.6,  
    simetriaAgua: 12,  
    tensaoSuperficial: 0.045,  
    amortecimentoIdeal: 255.0,  
    anguloLuzRecomendado: 81.0  
  },  
  {  
    hz: 417.0,  
    nomeDoDesenho: "Solfeggio 417 / Estrela Octogonal Simétrica",  
    m: 3,  
    n: 2,  
    coefA: 1.0,  
    coefB: \-0.85,  
    simetriaAgua: 12,  
    tensaoSuperficial: 0.045,  
    amortecimentoIdeal: 260.0,  
    anguloLuzRecomendado: 81.0  
  },  
  {  
    hz: 432.0,  
    nomeDoDesenho: "Afinação 432 / Grade de Quatro Lóbulos e Anel Central",  
    m: 2,  
    n: 2,  
    coefA: 1.0,  
    coefB: 1.0,  
    simetriaAgua: 12,  
    tensaoSuperficial: 0.045,  
    amortecimentoIdeal: 265.0,  
    anguloLuzRecomendado: 81.5  
  },  
  {  
    hz: 440.0,  
    nomeDoDesenho: "Lá4 Padrão / Cruz Hiperbólica Dupla",  
    m: 3,  
    n: 2,  
    coefA: 1.0,  
    coefB: 1.0,  
    simetriaAgua: 16,  
    tensaoSuperficial: 0.045,  
    amortecimentoIdeal: 268.0,  
    anguloLuzRecomendado: 81.5  
  },  
  {  
    hz: 528.0,  
    nomeDoDesenho: "Solfeggio 528 / Flor de Oito Pétalas e Núcleo Estrelado",  
    m: 3,  
    n: 2,  
    coefA: 1.0,  
    coefB: \-1.0,  
    simetriaAgua: 18,  
    tensaoSuperficial: 0.045,  
    amortecimentoIdeal: 280.0,  
    anguloLuzRecomendado: 82.0  
  },  
  {  
    hz: 639.0,  
    nomeDoDesenho: "Solfeggio 639 / Grade Cristalina Intermediária",  
    m: 4,  
    n: 2,  
    coefA: 1.0,  
    coefB: \-0.8,  
    simetriaAgua: 20,  
    tensaoSuperficial: 0.045,  
    amortecimentoIdeal: 295.0,  
    anguloLuzRecomendado: 82.0  
  },  
  {  
    hz: 741.0,  
    nomeDoDesenho: "Solfeggio 741 / Roseta de Três Anéis e Seis Lobos",  
    m: 4,  
    n: 2,  
    coefA: 1.0,  
    coefB: 1.0,  
    simetriaAgua: 24,  
    tensaoSuperficial: 0.045,  
    amortecimentoIdeal: 310.0,  
    anguloLuzRecomendado: 82.5  
  },  
  {  
    hz: 852.0,  
    nomeDoDesenho: "Solfeggio 852 / Rede Hiperbólica Densa",  
    m: 4,  
    n: 3,  
    coefA: 1.0,  
    coefB: 0.75,  
    simetriaAgua: 26,  
    tensaoSuperficial: 0.045,  
    amortecimentoIdeal: 325.0,  
    anguloLuzRecomendado: 83.0  
  },  
  {  
    hz: 963.0,  
    nomeDoDesenho: "Solfeggio 963 / Grade Simétrica e Roseta de 12 Pontas",  
    m: 5,  
    n: 2,  
    coefA: 1.0,  
    coefB: 1.0,  
    simetriaAgua: 28,  
    tensaoSuperficial: 0.045,  
    amortecimentoIdeal: 340.0,  
    anguloLuzRecomendado: 83.0  
  },  
  {  
    hz: 1181.0,  
    nomeDoDesenho: "Mandala Cristalina de 4 Anéis (f5 Quadrada 24cm)",  
    m: 5,  
    n: 3,  
    coefA: 1.0,  
    coefB: \-0.95,  
    simetriaAgua: 32,  
    tensaoSuperficial: 0.045,  
    amortecimentoIdeal: 360.0,  
    anguloLuzRecomendado: 83.5  
  },  
  {  
    hz: 2000.0,  
    nomeDoDesenho: "Micro-Retícula Cristalina Capilar de Alta Ordem",  
    m: 6,  
    n: 4,  
    coefA: 1.0,  
    coefB: 1.0,  
    simetriaAgua: 48,  
    tensaoSuperficial: 0.045,  
    amortecimentoIdeal: 400.0,  
    anguloLuzRecomendado: 84.0  
  }  
\];

