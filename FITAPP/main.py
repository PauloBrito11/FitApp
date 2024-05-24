import customtkinter as ctk
from PIL import Image

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1300x720")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # criar frame para o menu lateral
        self.sidebar_frame = ctk.CTkFrame(self, width=180, corner_radius=0)
        self.sidebar_frame.pack(side="left", fill="y")
        self.sidebar_frame.configure(fg_color="#292929")

        # carregar ícones 
        self.treinos_icon = self.load_icon("treinos.png")  # Use nomes de ícones apropriados
        self.exercicios_icon = self.load_icon("exercicios.png")
        self.dieta_icon = self.load_icon("dieta.png")

        # adicionar botões ao menu com ícones
        self.add_button("Treinos", self.treinos_icon, lambda: self.show_frame("Treinos"))
        self.add_button("Exercícios", self.exercicios_icon, lambda: self.show_frame("Exercícios"))
        self.add_button("Dieta", self.dieta_icon, lambda: self.show_frame("Dieta"))

        # armazenar o botão selecionado
        self.selected_button = None

        # criar frame para o separador vertical
        self.separator = ctk.CTkFrame(self, width=2, fg_color="#444444")
        self.separator.pack(side="left", fill="y")

        # criar frame para o conteúdo principal
        self.main_frame = ctk.CTkFrame(self, corner_radius=0)
        self.main_frame.pack(side="right", fill="both", expand=True)

        # dicionário para armazenar as telas
        self.frames = {}
        self.create_frames()

        # exibir a tela inicial
        self.show_frame("Treinos")  # mostrar a tela de Treinos inicialmente

    def add_button(self, text, icon, command):
        button = ctk.CTkButton(self.sidebar_frame, text=text,
                               image=icon, compound="left",
                               width=160, height=40,
                               command=lambda: self.select_button(button, command),
                               corner_radius=0,
                               fg_color="#242424",
                               hover_color="#e6bb67")
        button.pack(pady=5, padx=10)

    def select_button(self, button, command):
        if self.selected_button:
            self.selected_button.configure(fg_color="#242424")
        button.configure(fg_color="#e6bb67")
        self.selected_button = button
        command()

    def load_icon(self, filename):
        image = Image.open(filename).resize((20, 20))  # redimensionamento
        ctk_image = ctk.CTkImage(light_image=image, dark_image=image, size=(20, 20))  # Criar CTkImage
        return ctk_image

    def create_frames(self):
        self.frames["Treinos"] = ctk.CTkFrame(self.main_frame)

        # Tela de Exercícios com botões de grupos musculares (usando pack)
        self.frames["Exercícios"] = ctk.CTkFrame(self.main_frame)

        # Tela de Dieta com informações sobre macronutrientes e dicas (usando grid para layout)
        self.frames["Dieta"] = ctk.CTkFrame(self.main_frame)

        # PÁG 2 DE TREINOS
        self.frames["Dieta_pag_2"] = ctk.CTkFrame(self.main_frame)

        #PAG 2 EXERCÍCIOS
        self.frames["Exercícios_Proxima_Pagina"] = ctk.CTkFrame(self.main_frame)

        # rótulos e descrições de macronutrientes 
        ctk.CTkLabel(self.frames["Dieta"], text="Proteínas:", font=("Arial", 14, 'bold')).grid(row=0, column=0, padx=20, pady=10, sticky="w")
        descricao_proteinas = ctk.CTkTextbox(self.frames["Dieta"], width=350, height=50, border_color="#ffd58b", border_width=2)
        descricao_proteinas.insert("0.0", "Construção e reparo de tecidos, produção de enzimas e \n hormônios.")
        descricao_proteinas.configure(state="disabled")
        descricao_proteinas.grid(row=0, column=1, padx=20, pady=5)

        ctk.CTkLabel(self.frames["Dieta"], text="Carboidratos:", font=("Arial", 14, 'bold')).grid(row=1, column=0, padx=20, pady=5, sticky="w")
        descricao_carboidratos = ctk.CTkTextbox(self.frames["Dieta"], width=350, height=50, border_width=2, border_color="#ffd58b")
        descricao_carboidratos.insert("0.0", "Fonte primária de energia, poupam proteínas para funções estruturais.")
        descricao_carboidratos.configure(state="disabled") 
        descricao_carboidratos.grid(row=1, column=1, padx=20, pady=5) 

        ctk.CTkLabel(self.frames["Dieta"], text="Gorduras:", font=("Arial", 14, 'bold')).grid(row=2, column=0, padx=20, pady=5, sticky="w")
        descricao_gorduras = ctk.CTkTextbox(self.frames["Dieta"], width=350, height=50, border_width=2, border_color="#ffd58b") 
        descricao_gorduras.insert("0.0", "Reserva de energia, isolamento térmico, transporte de \nvitaminas.")
        descricao_gorduras.configure(state="disabled")
        descricao_gorduras.grid(row=2, column=1, padx=20, pady=5)

        ctk.CTkLabel(self.frames["Dieta"], text="Lipídios:", font=("Arial", 14, 'bold')).grid(row=0, column=10, padx=20, pady=10, sticky="w")
        descricao_lipidos = ctk.CTkTextbox(self.frames["Dieta"], width=350, height=50, border_color="#ffd58b", border_width=2)  # Criando um novo Textbox para Lipídios
        descricao_lipidos.insert("0.0", "Grupo diverso de moléculas orgânicas insolúveis em água, incluindo gorduras, óleos, ceras e esteroides. Funções semelhantes às gorduras.")  # Função dos lipídios
        descricao_lipidos.configure(state="disabled")
        descricao_lipidos.grid(row=0, column=11, padx=20, pady=5)

        ctk.CTkLabel(self.frames["Dieta"], text="Vitaminas:", font=("Arial", 14, 'bold')).grid(row=1, column=10, padx=20, pady=10, sticky="w")
        descricao_vitaminas = ctk.CTkTextbox(self.frames["Dieta"], width=350, height=50, border_color="#ffd58b", border_width=2)  # Criando um novo Textbox para Vitaminas
        descricao_vitaminas.insert("0.0", "Compostos orgânicos essenciais para o funcionamento normal do metabolismo, atuando como coenzimas e antioxidantes.")  # Função das vitaminas
        descricao_vitaminas.configure(state="disabled")
        descricao_vitaminas.grid(row=1, column=11, padx=20, pady=5)

        ctk.CTkLabel(self.frames["Dieta"], text="Minerais:", font=("Arial", 14, 'bold')).grid(row=2, column=10, padx=20, pady=10, sticky="w")
        descricao_minerais = ctk.CTkTextbox(self.frames["Dieta"], width=350, height=50, border_color="#ffd58b", border_width=2)  # Criando um novo Textbox para Minerais 
        descricao_minerais.insert("0.0", "Elementos inorgânicos essenciais para diversas funções, como formação de ossos e dentes, equilíbrio hídrico e atividade enzimática.")  # Função dos minerais
        descricao_minerais.configure(state="disabled")
        descricao_minerais.grid(row=2, column=11, padx=20, pady=5)

        # adicionando separador visual
        separador = ctk.CTkFrame(self.frames["Dieta"], height=2, fg_color="#444444")
        separador.grid(row=3, column=0, columnspan=300, pady=20, sticky = "NSEW")  

        # Dicas de alimentação
        dicas_label = ctk.CTkLabel(self.frames["Dieta"], text="Dicas de Alimentação para Hipertrofia:", font=("Arial", 16, 'bold'))
        dicas_label.grid(row=4, column=0, columnspan=2, pady=10)  
        dicas_text = """ 
        - Consuma proteínas de alta qualidade. 

        - Priorize carboidratos complexos. 

        - Inclua gorduras saudáveis. 

        - Hidrate-se adequadamente. 

        - Planeje suas refeições. 

        - Descanse e recupere-se. 

        - Coma alimentos que você gosta, para evitar que você fuja da dieta.  

        - Se não há a necessidade, evite entrar em dietas extremamente restritivas, é  
          possível ter ótimos resultados com dietas flexíveis. 

        - Calcule seu metabolismo basal. 

        - Priorize refeições com grandes quantidades de proteínas, para que possa  
          atingir sua meta diária de ingestão de proteínas. 

        - Não faça mudanças radicais em sua rotina repentinamente, a chance disso 
          tornar-se um hábito diminui consideravelmente. 
        """  
        dicas2_label = ctk.CTkLabel(self.frames["Dieta"], text="Dicas para manter uma dieta consistente:", font=("Arial", 16, 'bold'))
        dicas2_label.grid(row=4, column=10, columnspan=2, pady=10)  
        dicas2_text = """ 
        Comece Pequeno e Gradual: Não tente mudar tudo de uma vez. Introduza 
        pequenas mudanças na sua dieta e estilo de vida gradualmente 
        para aumentar as chances de sucesso a longo prazo. 

        Defina Metas Realistas e Alcançáveis: Evite metas extremas ou 
        restritivas demais. Estabeleça objetivos que se encaixem na 
        sua rotina e sejam sustentáveis a longo prazo.

        Planeje suas Refeições: Planeje suas refeições e lanches com 
        antecedência para evitar escolhas impulsivas e pouco 
        saudáveis quando estiver com fome.

        Faça Substituições Saudáveis: Troque alimentos processados 
        e ricos em açúcar por opções mais nutritivas, como frutas, 
        vegetais, grãos integrais e proteínas magras.

        Cozinhe em Casa com Mais Frequência: Cozinhar em casa permite controlar 
        os ingredientes e as porções, tornando mais fácil seguir sua dieta.

        Leia os Rótulos dos Alimentos: Preste atenção aos rótulos dos alimentos 
        para entender o valor nutricional e evitar ingredientes indesejados, 
        como açúcar adicionado, gorduras trans e excesso de sódio. 

        Mantenha-se Hidratado: Beba bastante água ao longo do dia para 
        manter-se hidratado e evitar confundir sede com fome.

        Priorize o Sono de Qualidade: Dormir o suficiente é fundamental 
        para regular os hormônios da fome e do apetite, facilitando a 
        adesão à dieta.

        Gerencie o Estresse: O estresse pode levar a escolhas alimentares 
        pouco saudáveis. Encontre maneiras de gerenciar o estresse, como 
        exercícios, meditação ou ioga.

        Seja Gentil Consigo Mesmo: Deslizes acontecem. Não se culpe por
        eventuais desvios da dieta. Aprenda com a experiência e volte 
        ao caminho certo.
        """

        dicas2_content = ctk.CTkTextbox(self.frames["Dieta"], width=500, height=200, border_width=2, border_color="#ffd58b")
        dicas2_content.insert("0.0", dicas2_text)
        dicas2_content.configure(state="disabled")
        dicas2_content.grid(row=5, column=10, columnspan=2, padx=20, pady=10)  

        dicas_content = ctk.CTkTextbox(self.frames["Dieta"], width=500, height=200, border_width=2, border_color="#ffd58b")
        dicas_content.insert("0.0", dicas_text)
        dicas_content.configure(state="disabled")
        dicas_content.grid(row=5, column=0, columnspan=2, padx=20, pady=10)  

        # Dicas de Desempenho Físico
        dicas_desempenho_label = ctk.CTkLabel(self.frames["Dieta"], text="Como ter um bom desempenho durante o treino:", font=("Arial", 16, 'bold'))
        dicas_desempenho_label.grid(row=6, column=0, columnspan=2, pady=10)  
        dicas_desempenho_text = """ 
        - Aqueça-se antes do treino e alongue-se depois. 

        - Priorize exercícios compostos (agachamento, supino, etc.). 

        - Progrida gradualmente na carga ou intensidade dos exercícios. 

        - Tenha um bom sono para recuperação muscular. 

        - Gerencie o estresse, pois ele pode afetar negativamente o desempenho. 

        - Experimente diferentes métodos de treino (HIIT, força, etc.). 

        - Ouça seu corpo e descanse quando necessário. 

        - Considere suplementos se necessário (proteína, creatina, etc.). 

        - Acompanhe seu progresso para se manter motivado.  
        """
        
        dicas_desempenho_content = ctk.CTkTextbox(self.frames["Dieta"], width=500, height=150, border_width=2, border_color="#e6bb67")
        dicas_desempenho_content.insert("0.0", dicas_desempenho_text)
        dicas_desempenho_content.configure(state="disabled")
        dicas_desempenho_content.grid(row=7, column=0, columnspan=2, padx=20, pady=10)  

        #importância da hidratação
        dicas_hidrataçao_label = ctk.CTkLabel(self.frames["Dieta"], text="Qual a importância da água?", font=("Arial", 16, 'bold'))
        dicas_hidrataçao_label.grid(row=6, column=10, columnspan=2, pady=10)   
        dicas_hidrataçao_text = """ 
        -Regulação da temperatura corporal: A água ajuda a regular a temperatura
        do corpo através da transpiração e evaporação, especialmente durante 
        atividades físicas ou em climas quentes.
        
        -Funcionamento adequado dos órgãos: A água é essencial para o 
        funcionamento adequado de órgãos vitais, como os rins, que 
        filtram resíduos do sangue,e o intestino, que precisa de 
        água para uma boa digestão.

        -Transporte de nutrientes: A água é um componente fundamental do sangue, 
        ajudando no transporte de nutrientes essenciais para as células do corpo.

        -Manutenção da pele saudável: A hidratação adequada ajuda a manter a pele 
        hidratada, prevenindo ressecamento, rugas e outros 
        problemas dermatológicos.

        -Melhora da função cognitiva: Estudos mostram que a desidratação 
        pode afetar negativamente a função cognitiva, incluindo a memória, 
        atenção e concentração.

        -Alívio da fadiga: A falta de água pode levar à fadiga, pois a desidratação 
        interferena eficiência do transporte de oxigênio e nutrientes para as 
        células, afetando a energia geral do corpo.

        -Prevenção de doenças: A hidratação adequada pode ajudar a prevenir 
        condiçõescomo cálculos renais, infecções do trato 
        urinário e constipação.

        -Desempenho físico: Durante o exercício, a hidratação é crucial para 
        manter o desempenho físico e a resistência, além de ajudar a 
        prevenir cãibras musculares.

        -Eliminação de toxinas: A água é essencial para o processo de excreção
        , ajudando o corpo a eliminar toxinas e resíduos metabólicos 
        através da urina e do suor.

        -Manutenção do equilíbrio hídrico: O corpo humano está constantemente 
        perdendo água através da respiração, transpiração e excreção, portanto,
        é importante  repor esse líquido perdido para manter o equilíbrio 
        hídrico e evitar a desidratação.  

        """
        dicas_hidrataçao_content = ctk.CTkTextbox(self.frames["Dieta"], width=500, height=150, border_width=2, border_color="#e6bb67")
        dicas_hidrataçao_content.insert("0.0", dicas_hidrataçao_text)
        dicas_hidrataçao_content.configure(state="disabled")
        dicas_hidrataçao_content.grid(row=7, column=10, columnspan=2, padx=20, pady=10)  

        botao_d2 = ctk.CTkButton(self.frames["Dieta"], text=">", command=lambda: self.show_frame("Dieta_pag_2"), width=5, height=10, font=("Arial", 18, 'bold'), border_width=2,fg_color='#ffd58b', text_color='#000000', border_color='#000000', hover_color='#FFFFFF')
        botao_d2.grid(row=4, column=15, columnspan=2, padx=0, pady=10)
        
        #---------------------------------------------PÁGINA DE DIETA PARTE 2

        ctk.CTkLabel(self.frames["Dieta_pag_2"], text="Creatina:", font=("Arial", 14, 'bold')).grid(row=0, column=0, padx=20, pady=10, sticky="w")
        descricao_creatina = ctk.CTkTextbox(self.frames["Dieta_pag_2"], width=350, height=50, border_color="#ffd58b", border_width=2)
        descricao_creatina.insert("0.0", "Aumenta a disponibilidade de energia para músculos, melhora a performance em exercícios de alta intensidade e curta duração.")
        descricao_creatina.configure(state="disabled")
        descricao_creatina.grid(row=0, column=1, padx=20, pady=5)

        ctk.CTkLabel(self.frames["Dieta_pag_2"], text="Whey Protein:", font=("Arial", 14, 'bold')).grid(row=1, column=0, padx=20, pady=5, sticky="w")
        descricao_whey = ctk.CTkTextbox(self.frames["Dieta_pag_2"], width=350, height=50, border_width=2, border_color="#ffd58b")
        descricao_whey.insert("0.0", "Proteína de rápida absorção, auxilia na recuperação e construção muscular após os treinos.")
        descricao_whey.configure(state="disabled") 
        descricao_whey.grid(row=1, column=1, padx=20, pady=5)

        ctk.CTkLabel(self.frames["Dieta_pag_2"], text="Hipercalóricos:", font=("Arial", 14, 'bold')).grid(row=2, column=0, padx=20, pady=5, sticky="w")
        descricao_hipercaloricos = ctk.CTkTextbox(self.frames["Dieta_pag_2"], width=350, height=50, border_width=2, border_color="#ffd58b")
        descricao_hipercaloricos.insert("0.0", "Fornecem grande quantidade de calorias e nutrientes, auxiliam no ganho de peso e massa muscular.") 
        descricao_hipercaloricos.configure(state="disabled")
        descricao_hipercaloricos.grid(row=2, column=1, padx=20, pady=5)

        ctk.CTkLabel(self.frames["Dieta_pag_2"], text="Pré-treino:", font=("Arial", 14, 'bold')).grid(row=0, column=10, padx=20, pady=10, sticky="w") 
        descricao_pre_treino = ctk.CTkTextbox(self.frames["Dieta_pag_2"], width=350, height=50, border_color="#ffd58b", border_width=2)
        descricao_pre_treino.insert("0.0", "Suplementos que aumentam a energia, o foco e a resistência durante os treinos.")
        descricao_pre_treino.configure(state="disabled")
        descricao_pre_treino.grid(row=0, column=11, padx=20, pady=5)

        ctk.CTkLabel(self.frames["Dieta_pag_2"], text="Consumo de água:", font=("Arial", 14, 'bold')).grid(row=1, column=10, padx=20, pady=10, sticky="w")
        descricao_agua = ctk.CTkTextbox(self.frames["Dieta_pag_2"], width=350, height=80, border_color="#ffd58b", border_width=2)
        descricao_agua.insert("0.0", "Um cálculo recomendado pelos especialistas é ingerir 35ml de água por cada quilo. Por exemplo, alguém que pesa 65 quilos deve tomar aproximadamente 2,27 litros de água por dia")
        descricao_agua.configure(state="disabled")
        descricao_agua.grid(row=1, column=11, padx=20, pady=5)

        consumo_whey_label = ctk.CTkLabel(self.frames["Dieta_pag_2"], text="Como consumir a Creatina", font=("Arial", 16, 'bold'))
        consumo_whey_label.grid(row=4, column=0, columnspan=2, pady=10) 
        consumo_whey_text = """ 
        Creatina: Entendendo o suplemento, seus efeitos e segurança

        A creatina é um composto orgânico naturalmente produzido pelo corpo e 
        também encontrado em alimentos como carne e peixe. Ela 
        desempenha um papel fundamental na produção de 
        energia para os músculos, especialmente durante 
        atividades de curta duração e alta intensidade. 
        A creatina também é um suplemento popular 
        entre atletas e praticantes de atividade 
        física, devido aos seus potenciais 
        benefícios para o desempenho e 
        a composição  corporal.

        Motivos para usar creatina:

        Aumento da força e potência: A creatina aumenta os estoques de fosfocreatina 
        nos músculos, que é utilizada para a produção rápida de energia durante 
        exercícios de alta intensidade. Isso pode resultar em melhorias na 
        força e potência muscular, permitindo treinos mais intensos e com 
        maior carga.

        Ganho de massa muscular: A creatina pode promover o crescimento muscular 
        através de diversos mecanismos, como aumento da síntese proteica, 
        retenção hídrica intramuscular e aumento da atividade de células 
        satélites.

        Melhora da recuperação muscular: A creatina pode auxiliar na recuperação 
        muscular após o exercício, reduzindo a dor e a inflamação.

        Benefícios para o cérebro: Estudos sugerem que a creatina pode ter 
        efeitos positivos sobre a função cognitiva, como memória e atenção.

        Síntese e fontes de creatina:

        A creatina é sintetizada no corpo a partir dos aminoácidos glicina, arginina
        e metionina. O fígado é o principal órgão responsável pela síntese de 
        creatina, seguido pelos rins e pâncreas. Além da produção endógena,
        a creatina também pode ser obtida através da dieta, 
        principalmente através do consumo de carne e 
        peixe.

        Segurança:

        A creatina é considerada um suplemento seguro quando utilizada nas doses 
        recomendadas. Estudos de longo prazo não demonstram efeitos adversos 
        significativos em indivíduos saudáveis. No entanto, alguns efeitos 
        colaterais leves podem ocorrer, como:

        Ganho de peso: A creatina pode causar retenção hídrica intramuscular, o 
        que pode resultar em um pequeno aumento de peso, principalmente no 
        início da suplementação.

        Problemas digestivos: Em algumas pessoas, a creatina pode causar 
        desconforto gastrointestinal, como inchaço e diarreia.

        Cãibras musculares: Embora não haja evidências científicas que comprovem 
        essa relação, alguns usuários relatam aumento da incidência de cãibras 
        musculares com o uso de creatina.

        Funcionamento no corpo:

        A creatina é armazenada nos músculos na forma de fosfocreatina. Durante 
        exercícios de alta intensidade, a fosfocreatina é utilizada para 
        regenerar o ATP (trifosfato de adenosina), que é a principal 
        fonte de energia para as células musculares. Ao aumentar 
        os estoques de fosfocreatina, a creatina permite que os 
        músculos produzam mais energia rapidamente, o que 
        resulta em melhorias na força, potência e 
        desempenho físico.

        Além disso, a creatina pode atuar como um agente de sinalização celular, 
        estimulando vias anabólicas que promovem o crescimento muscular.
        Em resumo, a creatina é um suplemento seguro e eficaz que pode 
        oferecer diversos benefícios para atletas e praticantes de 
        atividade física, como aumento da força, potência, massa 
        muscular e recuperação muscular. No entanto, é 
        importante consultar um profissional de saúde 
        antes de iniciar a suplementação, 
        especialmente se você tiver 
        alguma condição médica 
        pré-existente.

        """

        consumo_whey_content = ctk.CTkTextbox(self.frames["Dieta_pag_2"], width=500, height=200, border_width=2, border_color="#ffd58b")
        consumo_whey_content.insert("0.0", consumo_whey_text)
        consumo_whey_content.configure(state="disabled")
        consumo_whey_content.grid(row=5, column=0, columnspan=2, padx=20, pady=10)

        consumo_creatina_label = ctk.CTkLabel(self.frames["Dieta_pag_2"], text="Informações sobre o Whey Protein", font=("Arial", 16, 'bold'))
        consumo_creatina_label.grid(row=4, column=10, columnspan=2, pady=10) 
        consumo_creatina_text = """ 
        O whey protein, ou proteína do soro do leite, é um suplemento alimentar popular 
        entre atletas praticantes de atividade física e pessoas que buscam 
        aumentar a ingestão de proteínas Ele é derivado do soro do 
        leite, um líquido que se separa da coalhada durante o 
        processo de fabricação do queijo.

        Motivos para usar Whey Protein:

        - Aumento da massa muscular: O whey protein é rico em aminoácidos 
        essenciais, especialmente leucina, que desempenham um papel 
        crucial na síntese proteica muscular. Isso significa que ele 
        pode auxiliar no crescimento e reparação dos músculos
        após o exercício, favorecendo a hipertrofia.

        - Recuperação pós-treino: O whey protein é digerido e absorvido 
        rapidamente pelo corpo, fornecendo aminoácidos aos 
        músculos de forma eficiente, isso acelera a 
        recuperação muscular e reduz a dor após 
        os treinos.

        - Saciedade: Devido ao seu alto teor proteico, o whey protein 
        contribui para a sensação de saciedade, o que pode ajudar 
        no controle do apetite e na perda de peso.

        -Suplementação proteica: Para pessoas com dificuldade em atingir 
        as necessidades diárias de proteína através da 
        alimentação, o whey protein é uma forma 
        prática e conveniente de complementar 
        a ingestão proteica.

        Processo de fabricação:

        - O processo de fabricação do whey protein envolve diversas etapas:

        - Separação do soro do leite: O soro do leite é separado da coalhada 
        durante a produção do queijo.

        - Filtração: O soro do leite passa por processos de filtração para remover 
        a gordura, lactose e outros componentes indesejados.

        - Secagem: O soro filtrado é seco, geralmente por spray drying, resultando 
        em um pó concentrado de proteína.

        - Concentração: O whey protein pode ser ainda mais concentrado através de 
        processos como ultrafiltração ou microfiltração, aumentando
        o teor de proteína.

        Existem diferentes tipos de whey protein, cada um com 
        características específicas:

        -Concentrado de proteína do soro do leite (WPC): Contém entre 30% e 80% 
        de proteína, além de lactose e gordura.

        -Isolado de proteína do soro do leite (WPI): Contém mais de 90% de 
        proteína, com baixo teor de lactose e gordura.

        -Hidrolisado de proteína do soro do leite (WPH): A proteína é 
        pré-digerida, o que facilita a absorção pelo corpo.

        Segurança:

        O whey protein é considerado seguro para a maioria das pessoas quando
        consumido nas doses recomendadas. No entanto, alguns efeitos 
        colaterais podem ocorrer em indivíduos sensíveis, como:

        -Problemas digestivos: Gases, inchaço e diarreia podem ocorrer 
        em pessoas com intolerância à lactose. Optar pelo WPI ou WPH 
        pode minimizar esses efeitos.

        -Reações alérgicas: Embora raras, podem ocorrer reações alérgicas ao 
        whey protein, especialmente em pessoas com alergia ao leite.

        -É importante consultar um médico ou nutricionista antes de iniciar a 
        suplementação com whey protein, especialmente 
        se você tiver alguma condição médica 
        pré-existente.

        Funcionamento no corpo:

        Após a ingestão, o whey protein é digerido e quebrado em aminoácidos. 
        Esses aminoácidos são então absorvidos pelo intestino e 
        transportados para os músculos, onde sãoutilizados para 
        a síntese proteica. Esse processo é fundamental para a 
        recuperação e crescimento muscular.

        O whey protein também pode aumentar a liberação de hormônios anabólicos, 
        como a insulina, que promovem o crescimento muscular. Além disso, 
        pode auxiliar na redução dos níveis de cortisol, um hormônio 
        catabólico que pode levar à degradação muscular.

        Em resumo, o whey protein é um suplemento seguro e eficaz para aumentar
        a ingestão de proteína, auxiliar na recuperação muscular e promover 
        o crescimento muscular. No entanto, é importante consultar um 
        profissional de saúde antes de iniciar a suplementação.

        """

        consumo_creatina_content = ctk.CTkTextbox(self.frames["Dieta_pag_2"], width=500, height=200, border_width=2, border_color="#ffd58b")
        consumo_creatina_content.insert("0.0", consumo_creatina_text)
        consumo_creatina_content.configure(state="disabled")
        consumo_creatina_content.grid(row=5, column=10, columnspan=2, padx=20, pady=10)

        # adicionar separador visual
        separador = ctk.CTkFrame(self.frames["Dieta_pag_2"], height=2, fg_color="#444444")
        separador.grid(row=3, column=0, columnspan=300, pady=20, sticky="NSEW")

        # Botão "Próxima Página" (NAO UTILIZADO)
        #botao_d3 = ctk.CTkButton(self.frames["Treinos"], text=">", command=lambda: self.show_frame("Exercícios_Proxima_Pagina"), width=5, height=10, font=("Arial", 18, 'bold'), #border_width=2,fg_color='#ffd58b', text_color='#000000', border_color='#000000', hover_color='#FFFFFF')
        #botao_d3.grid(row=4, column=15, columnspan=2, padx=0, pady=10)

        # tela de Exercícios 

        botao_d4 = ctk.CTkButton(self.frames["Exercícios"], text=">", command=lambda: self.show_frame("Exercícios_Proxima_Pagina"), width=5, height=10, font=("Arial", 18, 'bold'), border_width=2,fg_color='#ffd58b', text_color='#000000', border_color='#000000', hover_color='#FFFFFF')
        botao_d4.grid(row=4, column=15, columnspan=2, padx=0, pady=10)
        
        Exercicio_grupo1_label = ctk.CTkLabel(self.frames["Exercícios"], text="Exercícios para o Peitoral?", font=("Arial", 16, 'bold'))
        Exercicio_grupo1_label.grid(row=6, column=10, columnspan=2, pady=10)  

        Exercicio_grupo1_text = """
         - Supino reto, com halteres/barra/máquina/smith
         - Supino inclinado, com halteres/barra/maquina/smith
         - Supino declinado, com halteres/barra
         - Crossover alto
         - Crossover baixo
         - Crossover reto
         - Flexão
         - Paralela
         - Pull-over
         - Crucifixo máquina 
         """
        Exercicio_grupo1_content = ctk.CTkTextbox(self.frames["Exercícios"], width=500, height=150, border_width=2, border_color="#e6bb67")
        Exercicio_grupo1_content.insert("0.0", Exercicio_grupo1_text)
        Exercicio_grupo1_content.configure(state="disabled")
        Exercicio_grupo1_content.grid(row=7, column=10, columnspan=2, padx=20, pady=10)  

        # Exercício_grupo2
        Exercicio_grupo2_label = ctk.CTkLabel(self.frames["Exercícios"], text="Exercícios para as Costas", font=("Arial", 16, 'bold')) 
        Exercicio_grupo2_label.grid(row=6, column=0, columnspan=2, pady=10)   

        Exercicio_grupo2_text = """ 
         - Remada serrote
         - Remada fechada máquina/polia
         - Remada cavalinho
         - Remada curvada aberta livre/máquina
         - Remada baixa com barra   
         - Pulley frente pegada pronada
         - Pulley frente pegada supinada
         - Puxada alta/pulldown
         - Crucifixo inverso
         - Levantamento terra
         - Barra fixa
         - Barra fixa pronada aberta
         - Barra fixa pronada/supinada com uma mão
         - Barra fixa pronada/supinada com uma mão utilizando elástico para suporte
         """
        Exercicio_grupo2_content = ctk.CTkTextbox(self.frames["Exercícios"], width=500, height=150, border_width=2, border_color="#e6bb67") 
        Exercicio_grupo2_content.insert("0.0", Exercicio_grupo2_text) 
        Exercicio_grupo2_content.configure(state="disabled") 
        Exercicio_grupo2_content.grid(row=7, column=0, columnspan=2, padx=20, pady=10)  

        # Exercício_grupo3
        Exercicio_grupo3_label = ctk.CTkLabel(self.frames["Exercícios"], text="Exercícios para o Triceps", font=("Arial", 16, 'bold')) 
        Exercicio_grupo3_label.grid(row=8, column=0, columnspan=2, pady=10)  

        Exercicio_grupo3_text = """ 
         - Triceps francês 
         - Triceps testa livre/polia/máquina
         - Triceps banco livre/máquina  
         - Triceps com barra reta, na polia alta
         - Triceps com corda, na polia alta
         - Triceps coice
         - Flexão
         - Flexão aberta
         - Flexão militar
         - Supino no banco, com pegada fechada
         - Triceps na paralela
         """ 
        Exercicio_grupo3_content = ctk.CTkTextbox(self.frames["Exercícios"], width=500, height=150, border_width=2, border_color="#e6bb67")  
        Exercicio_grupo3_content.insert("0.0", Exercicio_grupo3_text)  
        Exercicio_grupo3_content.configure(state="disabled")  
        Exercicio_grupo3_content.grid(row=9, column=0, columnspan=2, padx=20, pady=10)  

        # Exercício_grupo4 
        Exercicio_grupo4_label = ctk.CTkLabel(self.frames["Exercícios"], text="Exercícios para o Biceps", font=("Arial", 16, 'bold')) 
        Exercicio_grupo4_label.grid(row=8, column=10, columnspan=2, pady=10)  

        Exercicio_grupo4_text = """ 
         - Rosca direta, com barra/halteres/máquina
         - Rosca livre alternada, com barra/halteres/máquina
         - Rosca martelo com halteres/máquina
         - Rosca martelo alternada, com halteres
         - Rosca scott no banco
         - Rosca direta sentado, com halteres
         - Rosca martelo sentado, com halteres
         - Rosca concentrada com halteres no banco
         """ 
        Exercicio_grupo4_content = ctk.CTkTextbox(self.frames["Exercícios"], width=500, height=150, border_width=2, border_color="#e6bb67")  
        Exercicio_grupo4_content.insert("0.0", Exercicio_grupo4_text)  
        Exercicio_grupo4_content.configure(state="disabled")  
        Exercicio_grupo4_content.grid(row=9, column=10, columnspan=2, padx=20, pady=10)  

        # Exercício_grupo5 
        Exercicio_grupo5_label = ctk.CTkLabel(self.frames["Exercícios"], text="Exercícios para o Quadriceps", font=("Arial", 16, 'bold')) 
        Exercicio_grupo5_label.grid(row=10, column=0, columnspan=2, pady=10)  

        Exercicio_grupo5_text = """ 
         - Agachamento livre com barra
         - Agachamento livre
         - Agachamento no smith 
         - Agachamento com halteres
         - Agachamento sumo
         - Agachamento pistol (pistol squat)
         - Agachamento frontal
         - Agachamento búlgaro
         - Sissy squat
         - Cadeira extensora
         - Legpress 45
         """ 
        Exercicio_grupo5_content = ctk.CTkTextbox(self.frames["Exercícios"], width=500, height=150, border_width=2, border_color="#e6bb67")  
        Exercicio_grupo5_content.insert("0.0", Exercicio_grupo5_text)  
        Exercicio_grupo5_content.configure(state="disabled")  
        Exercicio_grupo5_content.grid(row=11, column=0, columnspan=2, padx=20, pady=10)  

        # Exercício_grupo6 
        Exercicio_grupo6_label = ctk.CTkLabel(self.frames["Exercícios"], text="Exercícios para a Posterior de Coxa", font=("Arial", 16, 'bold')) 
        Exercicio_grupo6_label.grid(row=10, column=10, columnspan=2, pady=10)  

        Exercicio_grupo6_text = """
         - Agachamento livre com barra
         - Agachamento livre
         - Agachamento no smith 
         - Agachamento com halteres
         - Agachamento sumo
         - Agachamento pistol (pistol squat)
         - Agachamento frontal
         - Agachamento búlgaro
         - Stiff, com barra/halteres
         - Stiff unilateral, com halteres
         - Levantamento terra
         - Cadeira flexora
         - Mesa flexora
         - Afundo com halteres
         """ 
        Exercicio_grupo6_content = ctk.CTkTextbox(self.frames["Exercícios"], width=500, height=150, border_width=2, border_color="#e6bb67")  
        Exercicio_grupo6_content.insert("0.0", Exercicio_grupo6_text)  
        Exercicio_grupo6_content.configure(state="disabled")  
        Exercicio_grupo6_content.grid(row=11, column=10, columnspan=2, padx=20, pady=10)  

        # Segunda tela de exercícios CONTEUDO --------------------------------------------------------------------------

        Exercicio_grupo7_label = ctk.CTkLabel(self.frames["Exercícios_Proxima_Pagina"], text="Exercícios para a Panturilha", font=("Arial", 16, 'bold')) 
        Exercicio_grupo7_label.grid(row=10, column=10, columnspan=2, pady=10)  

        Exercicio_grupo7_text = """
         - Elevação de panturilha em pé livre/máquina/smith
         - Gêmeos no burrinho 
         - Panturilha no legpress horizontal
         - Panturilha no legpress 45
         """ 
        Exercicio_grupo7_content = ctk.CTkTextbox(self.frames["Exercícios_Proxima_Pagina"], width=500, height=150, border_width=2, border_color="#e6bb67")  
        Exercicio_grupo7_content.insert("0.0", Exercicio_grupo7_text)  
        Exercicio_grupo7_content.configure(state="disabled")  
        Exercicio_grupo7_content.grid(row=11, column=10, columnspan=2, padx=20, pady=10)  

        Exercicio_grupo8_label = ctk.CTkLabel(self.frames["Exercícios_Proxima_Pagina"], text="Exercícios para o Ombro", font=("Arial", 16, 'bold')) 
        Exercicio_grupo8_label.grid(row=10, column=12, columnspan=2, pady=10)  

        Exercicio_grupo8_text = """
         - Elevação lateral, com halteres/polia/máquina
         - Elevação frontal, com halteres/polia
         - Crucifixo inverso, com halteres/máquina
         - Desenvolvimento com halteres
         """ 
        Exercicio_grupo8_content = ctk.CTkTextbox(self.frames["Exercícios_Proxima_Pagina"], width=500, height=150, border_width=2, border_color="#e6bb67")  
        Exercicio_grupo8_content.insert("0.0", Exercicio_grupo8_text)  
        Exercicio_grupo8_content.configure(state="disabled")  
        Exercicio_grupo8_content.grid(row=11, column=12, columnspan=2, padx=20, pady=10)  

        #

        #Tela de treinos:

        treinos1_label = ctk.CTkLabel(self.frames["Treinos"], text="ABC", font=("Arial", 16, 'bold'))
        treinos1_label.grid(row=6, column=10, columnspan=2, pady=10)   
        treinos1_text = """ 
        - Segunda-feira: A
        - Terça-feira: B
        - Quarta-feira C
        - Quinta-feira: A
        - Sexta-feira: B

        A ---> Peito, triceps e ombro
        B ---> Costas, biceps e deltoite anterior
        C ---> Perna

        """
        treinos1_content = ctk.CTkTextbox(self.frames["Treinos"], width=500, height=150, border_width=2, border_color="#e6bb67")
        treinos1_content.insert("0.0", treinos1_text)
        treinos1_content.configure(state="disabled")
        treinos1_content.grid(row=7, column=10, columnspan=2, padx=20, pady=10)  

        treinos2_label = ctk.CTkLabel(self.frames["Treinos"], text="ABC + 2X FULL BODY:", font=("Arial", 16, 'bold'))
        treinos2_label.grid(row=6, column=0, columnspan=2, pady=10)  
        treinos2_text = """ 
        - Segunda-feira: A
        - Terça-feira: B
        - Quarta-feira C
        - Quinta-feira: Full Body
        - Sexta-feira: Full Body

        A ---> Peito, triceps e ombro
        B ---> Costas, biceps e deltoite anterior
        C ---> Perna
        Full Body ---> Corpo completo, um exercício para cada músculo
        """
        
        treinos2_content = ctk.CTkTextbox(self.frames["Treinos"], width=500, height=150, border_width=2, border_color="#e6bb67")
        treinos2_content.insert("0.0", treinos2_text)
        treinos2_content.configure(state="disabled")
        treinos2_content.grid(row=7, column=0, columnspan=2, padx=20, pady=10)  

        # Treino 3
        treinos3_label = ctk.CTkLabel(self.frames["Treinos"], text="ABCDE", font=("Arial", 16, 'bold'))
        treinos3_label.grid(row=8, column=0, columnspan=2, pady=10) 

        treinos3_text = """
        - Segunda-feira: A
        - Terça-feira: B
        - Quarta-feira C
        - Quinta-feira: D
        - Sexta-feira: E

        A ---> Peito
        B ---> Costas
        C ---> Perna
        D ---> Braço
        E ---> Ombro 
        """
        treinos3_content = ctk.CTkTextbox(self.frames["Treinos"], width=500, height=150, border_width=2, border_color="#e6bb67")
        treinos3_content.insert("0.0", treinos3_text)
        treinos3_content.configure(state="disabled")
        treinos3_content.grid(row=9, column=0, columnspan=2, padx=20, pady=10)  

        # Treino 4
        treinos4_label = ctk.CTkLabel(self.frames["Treinos"], text="AB 2X na semana", font=("Arial", 16, 'bold'))
        treinos4_label.grid(row=8, column=10, columnspan=2, pady=10)  
        treinos4_text = """
        - Segunda-feira: A
         
        - Quarta-feira B
        
        - Sexta-feira: A

        A ---> Superiores completo
        B ---> Inferiores completo

        Para que todos os músculos sejam treinados em uma boa frequência,
        intercale entre começar com o treino A e começar com o treino B

        - Segunda-feira: B
         
        - Quarta-feira A
        
        - Sexta-feira: B
        """
        treinos4_content = ctk.CTkTextbox(self.frames["Treinos"], width=500, height=150, border_width=2, border_color="#e6bb67")
        treinos4_content.insert("0.0", treinos4_text)
        treinos4_content.configure(state="disabled")
        treinos4_content.grid(row=9, column=10, columnspan=2, padx=20, pady=10)  

        # Treino 5
        treinos5_label = ctk.CTkLabel(self.frames["Treinos"], text="ABCD", font=("Arial", 16, 'bold'))
        treinos5_label.grid(row=10, column=0, columnspan=2, pady=10)  

        treinos5_text = """
        - Segunda-feira: A 
        - Terça-feira: B
        - Quarta-feira: Descanso
        - Quinta-feira: C
        - Sexta-feira: D

        A ---> Costas + deltóide posteiror + bíceps
        B ---> Peito + deltóide anterior e medial + triceps
        C ---> Membros inferiores
        D ---> Membros superiores
        """
        treinos5_content = ctk.CTkTextbox(self.frames["Treinos"], width=500, height=150, border_width=2, border_color="#e6bb67")
        treinos5_content.insert("0.0", treinos5_text)
        treinos5_content.configure(state="disabled")
        treinos5_content.grid(row=11, column=0, columnspan=2, padx=20, pady=10)  

        # Treino 6
        treinos6_label = ctk.CTkLabel(self.frames["Treinos"], text="ABCDE variação", font=("Arial", 16, 'bold'))
        treinos6_label.grid(row=10, column=10, columnspan=2, pady=10)  

        treinos6_text = """
        - Segunda-feira: A
        - Terça-feira: B
        - Quarta-feira C
        - Quinta-feira: D
        - Sexta-feira: E

        A ---> Membros inferiores com ênfase em quadriceps + panturilha
        B ---> Peito + deltóide anterior e medial + triceps
        C ---> Costas + deltóide posterior + bíceps
        D ---> Membros inferiores com ênfase em glúteos e posterior + panturilha
        E ---> Superiores completo
        """
        treinos6_content = ctk.CTkTextbox(self.frames["Treinos"], width=500, height=150, border_width=2, border_color="#e6bb67")
        treinos6_content.insert("0.0", treinos6_text)
        treinos6_content.configure(state="disabled")
        treinos6_content.grid(row=11, column=10, columnspan=2, padx=20, pady=10)  
 
    def show_frame(self, frame_name):
        for frame in self.frames.values():
            frame.pack_forget()
        frame = self.frames[frame_name]
        frame.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = App()
    app.mainloop()