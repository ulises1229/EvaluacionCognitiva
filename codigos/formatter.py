#Formateador para clasificación de palabras
#Output deseado: ("El gato es amigo de ratón y perro", {"tags": []})
import spacy
import sys


def formmater(sentence, list_of_tags):
    formate = "(\"{}\", {{\"tags\":{}}})".format(sentence, list_of_tags)   # {42}
    print(formate)
    final_list.append(formate)
    #print(f'("{sentence}", ')

def definer(sentence, word):  #Función que devolverá J, V, N, D
    print("Para la oración: %s. y palabra: %s" % (sentence, word))
    new_val = input("Clasificar o escribir tag.\n"+
                    "1 -> Sustantivo\n"+
                    "2 -> Verbo\n"+
                    "3 -> Adverbio\n"+
                    "4 -> Adjetivo\n"+
                    "5 -> Dejar pronombre personal\n")
    try:
        new_v = int(new_val)
        if new_v == 1:
            return 'N'
        if new_v == 2:
            return 'V'
        if new_v == 3:
            return 'D'
        if new_v == 4:
            return 'J'
        if new_v == 5:
            return 'P'

    except IndexError:
        print('Error de index')
        pass

    except ValueError:
        return '%s' % new_val



nlp = spacy.load("es_core_news_md")

list_of_sentences = [
    "El gato es amigo de ratón y perro",
    "por que las pelotas son un juguete o aparato de distracción por lo tanto no tienen vida solo en Toy Story así que como no tienen vida no pueden cantar",
    "rima",
    "por que millonario canta",
    "por que al escucharse no tiene sentido",
    "la pelota salta no canta",
    "por que ninguna pelota cuando la rebotas no canta",
    "pelota es una metáfora para referirse a alguien con las cualidades",
    "pelota no puede cantar",
    "que mi hermano en redondo y grita mucho",
    "que es chillón",
    "el perro o el gato",
    "perro",
    "estambre",
    "el perro",
    "tu bello",
    "el perro o caballo",
    "tu perro",
    "gato perro ratón",
    "ratón",
    "la rabo de conejo" ,
    "hámster",
    "por que la soledad es un tesoro que se debe de aprovechar y usarse",
    "por que la copa de la liga mx es de plata",
    "por que un balín es como una pelota y es de color plata",
    "por que vale plata",
    "pelota padre",
    "moneda por que en es como una pelota y es redonda y vale y tienes que esforzaste para eso cuando rebotas una pelota tienes que mover las manos entonces para ganar el dinero lo mismo tienes que mover las manos para lograr eso mm es lógico verdad me voy lentamente",
    "que como es plata parece moneda o suena como una moneda",
    "pelota de plata",
    "creo que es una pelota color plata",
    "la luna tiene forma de pelota y es color plata",
    "mi papa es una pelota de plata porque el es el que genera mas plata dinero",
    "es redonda y tiene color plata",
    "la luna por que es redonda y color como gris",
    "algo que es de plata o que vale plata para ti",
    "por que es de color plata",
    "es una bola de color plata",
    "es de el color plata",
    "pues pelota de plata",
    "la luna es color plata y brilla",
    "qwewqe",
    "hrtehtrjjrey",
    "pues es una pelta color plata y mi chica",
    "pelota hecha de plata o color plata",
    "la luna es color plata",
    "porque es una cosa hecha de metal y es color plata",
    "puse luna por que es redonda y su color le tira al plateado siendo así una metáfora",
    "pelota fina",
    "si una pelota de fuego es el sol la de plata es la luna por ser blanca",
    "porque es blanca con gris y brilla la plata es mas o menos así",
    "una pelota color plata",
    "la luna por que es redonda y de color plata",
    "la luna es circular y de color plata",
    "la luna tiene un color muy singular que hace que a veces la veamos de color plata",
    "alguien que es fuerte o mercurio color plata",
    "Los amigos son muy valiosos, en mi opinión, como la plata, pero no se puede conseguir gratis y se puede aplicar una cicatriz a la misma, lo más importante antes de que puedas amar a un amigo. El oro significa que amarte a ti mismo es la primera cosa que debes hacer.",
    "la luna se ve como de plata o color plata y brilla en la noche",
    "de Zacatecas",
    "el cabello es de diferentes formas lacio chino crespo suave etc",
    "que se parece a Trevor",
    "nublosas",
    "de leches",
    "blanca",
    "greñudo",
    "picudo",
    "crespo",
    "vbsdhdsbhf invalida",
    "lacio y largo",
    "esponjaditas grandes de diferentes figuras",
    "el cabello es de un color verde y es puntiagudo",
    "feqrg",
    "con carne dentro y color como crema como amarillo y café mas o menos nombrándolo así y estas teclas no sirven",
    "carnuda",
    "flores de un color extravagante",
    "las flores de oro son iguales a el rocío de una rosa que es y que no es una flor de oro si lo tengo delante de mi leyendo esta frase de amor que han pasado",
    "portas",
    "brillosas",
    "suave o rígida depende de tu ADN molecular",
    "flores que brillan y que te llenan los ojos de alegría",
    "flores color amarillo o dorado",
    "flores duros con bonitas colores",
    "no por que los dientes son de marfil",
    "por brillan y los tiene blancos",
    "que las perlas brillan",
    "que brillan y son blancos",
    "de pura de seda",
    "seda",
    "flores de oro",
    "son flores color oro",
    "pues de oro perro",
    "son las flor de girasol",
    "flores del color del oro",
    "flores amarillo brillante",
    "una hermana rica okay no es una hermana tierna amable etc",
    "porque tal vez se llame candy",
    "efe",
    "son como el mio arduamente intenso y sonrojadamente destenso",
    "dulce linda amable",
    "dulce linda y simpática",
    "linda dulce y tierna",
    "una mirada que puede enamorarte o asustarte",
    "una sonrisa muy fría u okay no es una sonrisa fingida",
    "como sin ganas de reírte",
    "r4fwrg",
    "yes",
    "muy fría casi sin notarse",
    "tibia",
    "Colgate",
    "de flojera",
    "no solo que vivas en Alaska",
    "cuando comes hielo y se te congela la boca",
    "blanca y fría",
    "sin ganas como de que esta fastidiado art no tiene autoestima ni moral quizá tenga problemas no quiere hablar con nadie y quiere su espacio",
    "sonríes y te derrites",
    "bitter solor",
    "ocurre que se da mas la vegetación y naturaleza",
    "ftrjhu4j",
    "sol vacaciones y muchísimo calor",
    "viene Olaf y las mariposas y también las vacaciones",
    "los días son intensos que ocurren con los días miles de preguntas y cientos de respuestas albergan las calles de la soledad albergan delante mío de la sinofena tercera mía dejar las preguntas para después y mirar los días y años de la pesadumbre pasar lentamente ya pues no de pude arreglar ni cambiar tal vida miserable autor marco Antonio Gutiérrez león",
    "porque el gobierno no nos da nuestros impuestos",
    "llueve a cántaros",
    "es aburrido y tedioso como el Carol",
    "dormiste y sonaste con los angelitos",
    "juegos diversión pasamos todos en familia",
    "que no me quiere y quiere que conozca más personas para que me lastimen así como David que me dijo que le gustaba y a los dos días su novia es Nicole maldito año porque tardas mucho en terminar",
    "mas tiempo libre en el día",
    "que deja los mas valioso que tienes todo va y viene",
    "que si tienes un problema y se solucionara y mas después vendrán tiempos mejores tiempo de felicidad",
    "que llego mi tío navidad",
    "que ya es la fecha de navidad",
    "que ya es navidad",
    "que la navidad a llegado al país",
    "que la navidad ya llegó",
    "cuando pones tu árbol y adornos y te comprar regalos tu papa",
    "que la navidad llegó",
    "que es época de adviento",
    "es la época de navidad",
    "que los papás reyes están por llegar",
    "que navidad comienza",
    "que es navidad",
    "es navidad",
    "creo que estoy confundido por que los segundos no tienen a las a no ser que te refieras a que los segundos pasan muy rápido y eso si que es verdad pero bueno creo que e llegado al final así que adiós cuidate",
    "siempre tendremos un día malo pero eso no significa que nuestra vida sera mala todos pasamos por malos momentos eso es parte de la vida la vida se trata de como podemos recibir golpes y seguir adelante se trata de esforzarse",
    "que lo feo paso ahora viene lo chido feat Luis comunica",
    "que el festejo mas importante del año ya llego",
    "que la navidad llego",
    "que la navidad ya llego",
    "santa",
    "que es tiempo de celebrar la navidad",
    "que llego la navidad",
    "que la navidad esta por llegar",
    "ya es navidad",
    "que después de todo lo malo que sucedió el que escribió la frase tiene esperanza en un mejor futuro",
    "que ha llegado la época de la navidad en la que como bien rico y mis papás me dan juguetes y la comida esta bien bien rica y me encanta el pavo por si querían saber",
    "el nacimiento de dios en la tierra"
    "que después de todo lo malo vendrán tiempos mejores con mas felicidades etc",
    "y santa Claus bajo",
    "que ya es navidad o va a ser navidad",
    "que la navidad ya esta aquí",
    "estamos en época de navidad",
    "que por fin es navidad",
    "que es hora de festejar la navidad" ,
    "que la navidad llego regalos comida familia o soledad hay de todo en este mundo",
    "que ya estamos en navidad presente",
    "que es el día de navidad y habrá cena regalos etc",
    "que ya es tiempo de navidad y regalos y cosas así",
    "hay mucho amor en la casa y esta toda mi familia conmigo y es divertido",
    "que llegó navidad",
    "que la navidad ya esta",
    "que ha llegado el frio y pues también algunas personas a enfermarse",
    "año nuevo y llegan regalos",
    "que al fin es navidad",
    "llega la época de navidad",
    "que ahora es navidad",
    "que los segundos van tan rápido y que por mas rápido que van el no me ama solo ama a su novia pero que se puede esperar debí de hacer caso cuando Lilí me dijo que era solo un juguete pero no hay voy de mensa a caer en sus redes tan fácilmente deberían de darme un óscar por ilusionarme rápido y a el otro por ser un romper corazones excelente y ilusionador",
    "que ya esta aquí la navidad",
    "que ya es navidad o que las personas ya empezaron a decorar sus casas",
    "que empieza navidad",
    "santa Claus o regalos",
    "que el tiempo paso muy rápido que ya hace un año estábamos en navidad y pues llego rápido",
    "que aun faltan mas cosas buenas por venir",
    "que ya falta poco o ya es navidad",
    "que ya es la fecha de navidad o que ya se tiene espíritu navideño",
    "llego la día mas feliz del año que todas las personas celebran",
    "el día de la navidad estaba aquí",
    "la es época de navidad",
    "que la época de navidad ya esta y Jesús nace",
    "que la navidad esta aquí",
    "que la fecha de navidad llego",
    "que brillan",
    "que las estrellas brillan mas que ayer",
    "que mis ojos o sus ojos son muy lindos",
    "puede tener ojos de color pero de miel no",
    "por que Yolo",
    "que las estrellas brillan",
    "por que brillan",
    "todo puede ser posible solo que los de miel serian solo en caricaturas una fantasía",
    "que son bellas y brillan tanto como si fueran de cristal",
    "no porque las estrellas están a millones de kilómetros y son esferas de gas que se van consumiendo asta explotar y convertirse en ya sea una estrella de protones o una súper nova",
    "por que brillan y se podría decir que son de cristal",
    "por que la estrella brilla y se ve como cristal",
    "por que las estrellas son muy posibles en hacerse como las de navidad",
    "sonando todo se puede amor mio",
    "porque puedes ejercitarte para tener unas piernas fuertes",
    "porque el orden de una materia no puede ser alterado por otra a menos de que ya exista un ADN que pueda alterar las moléculas humanas y metálicas",
    "porque cuando describes alguien con ojos amarillo y café decimos ojos de miel",
    "pro que brillan",
    "porque esas brillan",
    "no porque las estrellas están hechas de pequeños asteroides",
    "porque el color miel sale del color café pero muy claro",
    "porque hay ojos color miel mas no hay ojos de miel",
    "porque es imposible tener ojos hechos de miel pero si color miel",
    "porque decir ojos de miel es figurado nadie puede tener ojos hechos de miel",
    "wqb",
    "una hoja doblada en varias partes",
    "que si es posible yo he visto uno y tengo uno en casa no es mio pero lo tengo y lo he sentido",
    "la piel no puede ponerse en sobres o no que yo sepa", 
    "un papel que esta doblado en varias partes y se puede meter alguna carta",
    "son pequeñas esferas que se encuentran en el mar en un animal llamado almeja",
    "por que es donde meten una carta para mandársela a una personas que están lejos",
    "las perlas se pueden hacer collar",
    "por que lo mas común es hacer un vestido de un material suave tela",
    "que un zapato es como miel dulce",
    "un zapato de miel",
    "que los zapatos estén creados de pura miel",
    "que yo dijo que no por lo que e vis ay de cuero",
    "un zapato cubierto de miel",
    "que te largues",
    "todos lo meses de el año de Zacatecas",
    "que es un calendario hecho de zacate",
    "el ocnitrix",
    "escoba fina",
    "escoba echa de cristal",
    "escobas finas o delicadas",
    "miel con forma de zapatos",
    "escobas hechas de cristal",
    "escobas pero al lugar de los pelos es cristal",
    "escobas que están duras",
    "pues que pisaste miel",
    "que los zapato son de miel",
    "que pueden llenarse de miel",
    "zapato de cuero cubierto con miel",
    "que no es posible hacer un calendario de zacate",
    "escobas muy delicadas",
    "es una herramienta que tienes en casa para poder asearla casa limpiarla",
    "calendario para bañarte",
    "no no es posible es como si ella me amara",
    "pueden ser creados parte de ellos con miel",
    "no se puede hacer de zacate",
    "para bañarse",
    "la miel se derrite y unos zapatos de miel no son muy cómodos",
    "porque el zacate es algo que usas para bañarte",
    "si es posible que le caiga miel de abeja a tus zapatos pero muy improbable",
    "no es posible ya que una escoba debe estar hecha de fibras para que pueda recoger y empujar partículas de polvo",
    "por que si es puede ser el zapato de miel",
    "no es posible por que los zapatos de miel serian incómodos y pegajosos",
    "porque el zacate es duro y grueso y porque nadie ocupa un calendario para bañarse también no se podría imprimir las letras en un zacate",
    "pues por que no camino",
    "porque un zacate es con lo que te tallas al bañarte a menos que tenga otro significado que no sepa y pues un calendario donde ves fechas",
    "por que no puedes hacer zapatos de miel ya que la miel es liquida",
    "porque no pueden ser literalmente de miel mas se puede ocupar como una expresión",
    "porque no le veo ningún sentido a calendario de zacate",
    "porque nadie dijo que tuviéramos que imprimirlo en la hierba seca, sólo dice que hay que crear una calandario, así que si la creas de una manera diferente, todo es posible.",
    "el carbón quema",
    "carbón ardiente es un pedazo de madera",
    "que es lo que comes durante todo el día y lo dulce es normalmente en el desayuno por ejemplo el pan y en salado pues carnes mariscos",
    "que no se entiende lo que escribes",
    "que el carbón quema",
    "que las estatuas de la isla de pascua",
    "un carbón son como piedras para que pendra y se quede prendida una fogata",
    "por que algunas veces se nos puede ir la mano por eso es mejor medirla antes de agregarla",
    "que no es dulce bruh cier",
    "comida que no es dulce que puedes comer o es de limón chile etc",
    "por que casi todas las esculturas son de hierro o piedra no hay mas a menos que seas rico y hagas una de hora",
    "si por que la modifican",
    "si porque puede hacer que la comida sepa salado o por los ingredientes que tienen",
    "escencija",
    "porque hay gente que por mas que intentes su letra no mejorara y jamas se le entenderá",
    "si por que en las plazas centro casa y lugares turísticos al igual que en museos las ahí",
    "si ya que da a entender que no solo hay esculturas de metal bronceo plata u incluso oro sino que variedad es extensa",
    "por ay muchas y mas grandes",
    "si porque así como hay esculturas de bronce plata oro puede a ver de piedra y de mucho mas",
    "si por que cuando haces fogatas o lumbre le pones carbón y arde",
    "porque en personas se pueden equivocar y echar sal marina para que sepa así",
    "porque a veces se te olvida y le pones mas de la necesaria",
    "un abrazo dice mas que mas mil palabras",
    "que no importa como des el abrazo el valor no cambia",
    "que te abrazan sin apretarte",
    "Donald Trump",
    "que los abrazos que te dan o das son suaves que no son fuertes",
    "abrazo no tan fuerte",
    "que la persona es tan cruel que no sabe apreciar a alguien mas sino que solo se interesa en el y en su vida que no tanto tiempo para pensar en el daño que lesa hace alas personas que lo quieren o lo aprecian",
    "pues que tiene su alma muy fuerte perro",
    "mm pues una una alma de hierro o sea dura",
    "una alma a la que no le duele nada",
    "que no hay almas de hierro mas adelante las podrían crear",
    "indea",
    "si por que hay gente muy cruel como Hitler que tenia un alma de hierro era muy cruel",
    "por que las al mas no se pueden tocar",
    "sor no descansarlos",
    "si por que hay personas alas que no les gusta que las abrasen fuerte",
    "depende de tus fuerzas",
    "porque he visto a Donald Trump",
    "porque aquel que ha perdido mucho y ademas ha resistido es porque el tiene mucha fuerza interior",
    "no por que mas que una persona sea mala también tiene sentimientos",
    "por que por mas que una persona sea mala todos los seres humanos tenemos sentimientos",
    "no es posible por que el alma es transparente a menos que digas mi alama es de hierro",
    "si llega a pasarnos a todas las personas mas si eres muy estresante",
    "porque se pu",
    "una banqueta no puede abrigarte",
    "calceta dura",
    "los lapices sin sabor no son mas que lapices ordinarios en cambio el lápiz del sabor solo se muestran ante verdaderos escritores y a personas cultas del arte",
    "que el lápiz no tiene sabor",
    "que un lápiz no es de sabor",
    "que los lápiz no tienen sabor",
    "que el lápiz no sabe a nada",
    "que el lápiz esta hecho de madera y la madera tiene sabor",
    "plata mineral",
    "que el lápiz no tiene sabor pero la mayoría de los lápices tienen sabor por que viene de la madera después le ponen como pintura y eso le da como sabor feo pero tiene sabor",
    "lápiz sin punta",
    "que hay una cosa con la que se hace el lápiz que o tiene sabor",
    "que el lápiz no escribe pues no le puede usar",
    "lápiz con un sabor ejemplo fresa",
    "nada",
    "calceta color plateada",
    "que la calceta es color plata",
    "bueno pues una calceta color plata",
    "lápiz que no sabe a nada si lo pruebas",
    "que el lápiz no pinta bien",
    "sabe a lo que a tocado ese lápiz",
    "metafóricamente el lápiz no dibuja con el sabor necesario para transmitir algo",
    "lápiz amargo",
    "que el lápiz no pinta",
    "que hay lápiz que no tienen sabor y ay otros que si tienen sabor",
    "calceta color plata",
    "calceta hecha de plata",
    "por que todo tiene sabor color y olor por mas mínimo que sea",
    "lápiz que no sabe a nada",
    "el lápiz tiene sabor de lo que esta hecho",
    "que el lápiz no pinta bien o su color no es bueno",
    "calceta hecha con plata",
    "que el lápiz no sabe a nada si lo muerdes",
    "que el lápiz no tiene ningún sabor si te lo metes en la boca",
    "si porque dios creo todo el mundo",
    "no no",
    "no es posible por que los lápiz no tienen sabor",
    "porque cuando muerdes un lápiz va a tener a fuerzas un sabor ni modo que la madera no tenga un sabor",
    "no por que todos los materiales con los que elaboran el lápiz tienen algún sabor",
    "es para escribir",
    "no por que el lápiz no tiene sabor",
    "que yo sepa no existen calcetines de plata",
    "si es posible porque todo tiene sabor y el lápiz también",
    "si porque mi lápiz es así",
    "pues creo que no porque pues una calceta no puede ser hecha de plata menos que la rellenes de plata",
    "porque el lápiz no sirve",
    "porque lamo los lapices",
    "no es posible porque el autor es el que transmite el sentimiento no el lápiz",
    "por que un lápiz pues tiene un sabor a madera",
    "por que ningún lápiz tiene sabor si no son de dulce",
    "porque puedes decir cosas si sentido no se refiere que el lápiz tenga sabor o no",
    "no por que el lápiz no tienen sabor",
    "si por que los lápiz no tienen sabor",
    "no por que un lápiz esta hecho para escribir no para chupar",
    "porque te va a hacer sentir con mas confianza en ti misma",
    "por que yo tengo calcetas color plata",
    "si el lápiz esta hecho de madera y la madera tiene sabor",
    "no porque si la calceta sera de plata nadie va a poder usarlo",
    "porque si muerdes un lápiz no va a saber a nada",
    "a que una silla ya se desocupo",
    "que la silla ya llego para que esperes y esperes algo sentada en ella",
    "porque llego tu novia a tu casa",
    "la cebolla llega a las manos del cachador después de un excelente lanzamiento por parte del pichador",
    "que cala mucho cuando picas",
    "una m mccosciuspu",
    "que los de DHL te trajeron una silla",
    "el sol y el Hitler",
    "porque en este planeta el valor que mas se sigue es la flojera",
    "porque Liverpool te puede traer una silla",
    "que se las anel viado",
    "que comes cebolla",
    "pues como cala es muy fuerte para ti",
    "por que yolo",
    "pelota cebolla",
    "por que esta escrito en la biblia",
    "nod",
    "porque no te bañaste o no cepillaste los dientes",
    "porque huele fuerte",
    "que Liverpool ya trajo su silla",
    "cuando faltan traen mas",
    "si porque cuando partes cebolla lloras",
    "por que empiezas a cortar la cebolla y lloras",
    "si porque cala en los ojos",
    "llego en las compras",
    "si por que cuando la avientas roda entonces puede llegar a ti",
    "por que un orno no tiene movilidad propia",
    "si ya desocupo",
    "que los hornos de están moviendo mas cerca uno del otro",
    "porque son atletas perro",
    "que pueden estar por lo aires",
    "el tren transporta gente",
    "que las personas que son atletas pues corren y deben tener la habilidad para hacerlo e ir mejorando cada día mas",
    "que el ave vuela",
    "que una gaviota ave vuela",
    "que el tren esta transportándose",
    "si perro",
    "Minecraft",
    "por que en ellos viajan personas y ellos igual perro",
    "así es como trabaja el tren",
    "porque gente como Usain Bolt existen",
    "todos tienen el derecho a la libertad el ave volando es un símbolo de libertad mundial",
    "si y mas si es atleta por que ellos se especializan en eso",
    "por que así las hizo dios",
    "por que eyaqs debe volar",
    "si porque alguna personas usan el tren para poder trasladarse de un lugar a otro",
    "si porque tu te mueves y corres mas los atletas",
    "si eres atleta corres",
    "que pongan mas tiempo en la escuela",
    "que la ya va a ser la noche y va a empezar a oscurecerse",
    "and fort mach",
    "que el tiempo en realidad esta ya sea contigo a tu ritmo o correteándote y a veces te alcanza",
    "que es ora de dormir en tu colchón spring air",
    "que cobos corre",
    "que es mas que suficiente el tiempo",
    "entre mas tardes mas tiempo necesitaras",
    "siper",
    "por que si te tardas el tiempo te alcanza ejemplo Ana tiene que salir a las tres y son las dos y media y se tarda jugando media hora entonces el tiempo la alcanza por que ya son las tres",
    "si por que en la biblia",
    "porque el día dura 12 horas y la noche 12 horas",
    "es posible porque lo veo todos los días y me duermo bien rico y se siente delicioso y ademas me despiertan demasiado temprano para ir a la escuela en la que nos ponen encuestas bien chidas como esta se murió Robin Williams",
    "por que sabiéndote organizar si te alcanza el tiempo",
    "si por el ejemplo que di hace rato",
    "por que el planeta tierra esta en constante rotación por lo que llega la noche",
    "si es posible porque la frase es usada para referirse a que el tiempo es suficiente",
    "es una expresión muy conocida ademas tiene sentido tal y como lo dices",
    "porque mientras mas tarde es mas noche es"
]

final_list = []
#sys.exit("Fin de ejecución")

#list_unknown = []

for sentence in list_of_sentences:
    #print("Vaciando lista de tags")
    list_of_tags = []
    #print("Analizando: ",sentence) #oración
    analysis = nlp(sentence)
    for token in analysis:
        #print(token.pos_) #tipo de palabra
        if token.pos_ == "SCONJ":
            list_of_tags.append("SC")
        elif token.pos_ == "ADV":
            list_of_tags.append("D")
        elif token.pos_ == "VERB":
            list_of_tags.append("V")
        elif token.pos_ == "ADJ":
            list_of_tags.append("J")
        elif token.pos_ == "NOUN":
            list_of_tags.append("N")
        elif token.pos_ == "AUX":
            list_of_tags.append("AX")
        elif token.pos_ == "DET":
            list_of_tags.append("DT")
        elif token.pos_ == "CONJ":
            list_of_tags.append("CN")
        elif token.pos_ == "nsubj":
            list_of_tags.append("NSUB")
        elif token.pos_ == "ADP":
            list_of_tags.append("ADP")
        elif token.pos_ == "nmod":
            list_of_tags.append("NMD")
        elif token.pos_ == "PUNCT":
            list_of_tags.append("PCT")
        elif token.pos_ == "obl":
            list_of_tags.append("OBL")
        elif token.pos_ == "INTJ":
            list_of_tags.append("ITJ")
        elif token.pos_ == "PRON":
            list_of_tags.append("PRN")
        elif token.pos_ == "PART":
            list_of_tags.append("PRT")
        elif token.pos_ == "NUM":
            list_of_tags.append("NM")
        elif token.pos_ == "PROPN":
            new_tag = definer(sentence, token)
            list_of_tags.append(new_tag)
        else:
            print("Otro pos:", token.pos_)
            list_unknown.append(token.pos_)
            list_unknown.append(sentence)
            
    
    formmater(sentence, list_of_tags)

print("Lista desconocidos: ", list_unknown)
with open('training_data.txt', 'w', encoding="latin1") as f:
        for item in final_list:
            f.write("%s\n" % item)