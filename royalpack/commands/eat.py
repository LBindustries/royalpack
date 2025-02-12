from royalnet.commands import *


class EatCommand(Command):
    name: str = "eat"

    description: str = "Mangia qualcosa!"

    syntax: str = "{cibo}"

    _FOODS = {
        "_default": "🍗 Hai mangiato {food}!\n[i]Ma non è successo nulla.[/i]",
        
        # Sezione nonna
        "tutto": "👵🏻 Hai mangiato {food}. Si vede che hai gradito il pasto!\n[i]Tua nonna ti serve un'altra"
                 " porzione.[/i]",
        "poco": "👵🏻 Hai mangiato davvero {food}! \n[i]Tua nonna è molto arrabbiata e ferita nell'orgoglio."
                " Vergognati![/i]",
        "nonna": "👵🏻 Hai mangiato tua {food}. In qualche modo, continua a cucinarti cibo anche da dentro la"
                 " pancia.\n[i]This can't end well...[/i]",
        "qualcosa di non cucinato dalla nonna": "👵🏻 Hai mangiato {food}!\n[i]Potresti essere appena stato "
                                                "diseredato...[/i]",
        "qualcosa di non preparato dalla nonna": "👵🏻 Hai mangiato {food}!\n[i]Potresti essere appena stato "
                                                "diseredato...[/i]",
        
        # Sezione caffé (ce n'erano troppi, con gli accenti e il resto)
        "caffè": "☕️ Oh, no! Questo era il {food} della Peppina!\n[i]Ha provato col tritolo, salti in aria col"
                 " {food}.[/i]",
        "caffé": "☕️ Oh, no! Questo era il {food} della Peppina!\n[i]Ha provato col tritolo, salti in aria col"
                 " {food}.[/i]",
        "caffe": "☕️ Oh, no! Questo era il {food} della Peppina!\n[i]Ha provato col tritolo, salti in aria col"
                 " {food}.[/i]",
        "kaffee": "☕️ Ma BUONGIORNISSIMOOO !!!!\n[i]Non si può iniziare la giornata senza un buon {food} !![/i]",
        "kaffè": "☕️ Ma BUONGIORNISSIMOOO !!!!\n[i]Non si può iniziare la giornata senza un buon {food} !![/i]",
        "kaffé": "☕️ Ma BUONGIORNISSIMOOO !!!!\n[i]Non si può iniziare la giornata senza un buon {food} !![/i]",
        "kaffe": "☕️ Ma BUONGIORNISSIMOOO !!!!\n[i]Non si può iniziare la giornata senza un buon {food} !![/i]",
        
        # Sezione in cui mangi i membri Royal Games
        "balu": "🚹 Hai mangiato {food}.\n[i]Sa di snado.[/i]",
        "evilbalu": "🚹 Hai mangiato {food}.\n[i]Sa di snado.[/i]",
        "balubis": "🚹 Hai mangiato {food}.\n[i]Sa di acqua calda.[/i]",
        "goodbalu": "🚹 Hai mangiato {food}.\n[i]Sa di acqua calda.[/i]",
        "chiara": "🚺 Hai mangiato {food}.\n[i]Sa un po' di biscotto, ma per lo più sa di curcuma, pepe e spezie"
                  " varie.[/i]",
        "fabio": "🚹 Hai mangiato {food}.\n[i]Sa di gelatina tuttigusti+1.[/i]",
        "proto": "🚹 Hai mangiato {food}.\n[i]Sa di gelatina tuttigusti+1.[/i]",
        "marco": "🚹 Hai mangiato {food}.\n[i]Sa di carlino <.<[/i]",
        "mallllco": "🚹 Hai mangiato {food}.\n[i]Sa di carlino <.<[/i]",
        "max": "🚹 Hai mangiato {food}.\n[i]Sa di merda.[/i]",
        "maxsensei": "🚹 Hai mangiato {food}.\n[i]Sa di merda.[/i]",
        "steffo": "🚹 Hai mangiato {food}.\n[i]Sa di gelato e di Coca-Cola.[/i]",
        
        #Sezione delle supercazzole
        "antani": "Hai mangiato {food}. \n[i]Con tarapia tapioco o scherziamo? No, mi permetta. Noi siamo in 4."
        "Come se fosse antani anche per lei soltanto in due, oppure in quattro anche scribàcchi confaldina?"
        "Come antifurto, per esempio.[/i]",
        "indice": "Hai mangiato l'{food}. \n[i]Ecco, lo alzi. Lo vede, lo vede che stuzzica?[/i]",
        
        # Altro
        "tonnuooooooro": "👻 Il {food} che hai mangiato era posseduto.\n[i]Spooky![/i]",
        "uranio": "☢️ L'{food} che hai mangiato era radioattivo.\n[i]Stai brillando di verde![/i]",
        "pollo": '🍗 Il {food} che hai appena mangiato proveniva dallo spazio.\n[i]Coccodè?[/i]',
        "ragno": "🕸 Hai mangiato un {food}.\n[i]Ewww![/i]",
        "curry": "🔥 BRUCIAAAAAAAAAA! Il {food} era piccantissimo!\n[i]Stai sputando fiamme![/i]",
        "peperoncino": "🔥 BRUCIAAAAAAAAAA! Il {food} era piccantissimo!\n[i]Stai sputando fiamme![/i]",
        "torta": "⬜️ Non hai mangiato niente.\n[i]La {food} è una menzogna![/i]",
        "cake": "⬜️ Non hai mangiato niente.\n[i]The {food} is a lie![/i]",
        "biscotto": "🍪 Hai mangiato un {food} di contrabbando.\n[i]L'Inquisizione non lo saprà mai![/i]",
        "biscotti": "🍪 Hai mangiato tanti {food} di contrabbando.\n[i]Attento! L'Inquisizione è sulle tue tracce![/i]",
        "tango": "🌳 Hai mangiato un {food}, e un albero insieme ad esso.\n[i]Senti le tue ferite curarsi...[/i]",
        "giaroun": "🥌 Il {food} che hai mangiato era duro come un {food}.\n[i]Stai soffrendo di indigestione![/i]",
        "giarone": "🥌 Il {food} che hai mangiato era duro come un {food}.\n[i]Stai soffrendo di indigestione![/i]",
        "sasso": "🥌 Il {food} che hai mangiato era duro come un {food}.\n[i]Stai soffrendo di indigestione![/i]",
        "gnocchetti": "🥘 Ullà, sono duri 'sti {food}!\n[i]Fai fatica a digerirli.[/i]",
        "tide pod": "☣️ I {food} che hai mangiato erano buonissimi.\n[i]Stai sbiancando![/i]",
        "tide pods": "☣️ I {food} che hai mangiato erano buonissimi.\n[i]Stai sbiancando![/i]",
        "gelato": "🍨 Mangiando del {food}, hai invocato Steffo.\n[i]Cedigli ora il tuo gelato.[/i]",
        "tua mamma": "⚠️ Non sei riuscito a mangiare {food}.\n[i]Era troppo grande e non ci stava nella tua bocca![/i]",
        "mango": "🥭 Hai mangiato un {food}.\n[i]Ti sembra di avere più mana, adesso.[/i]",
        "mango incantato": "🥭 Hai mangiato un {food}.\n[i]Ti sembra di avere più mana, adesso.[/i]",
        "enchanted mango": "🥭 Hai mangiato un {food}.\n[i]Ti sembra di avere più mana, adesso.[/i]",
        "musica": "🎶 Hai mangiato un po' di {food} mentre ascoltavi un buon pranzo.\n[i]Tutto ciò ha perfettamente"
                  " senso.[/i]",
        "fungo": "🍄 Hai mangiato un {food}.\n[i]Presto riuscirai a salvare Peach![/i]",
        "zucca": "🎃 Hai mangiato una {food}. Solo che era una lanterna di Halloween.\n[i]Inizi a fare luce al"
                 " buio.[/i]",
        "granchio": "🦀 Hai mangiato un {food}. {food} is gone!\n[i]Senti il tuo stomaco ballare.[/i]",
        "crab": "🦀 Hai mangiato un {food}. {food} is gone!\n[i]Senti il tuo stomaco ballare.[/i]",
        "veleno": "☠️ Hai mangiato del {food}. Perché lo hai fatto?\n[i]Adesso stai male, contento?[/i]",
        "polvere": "☁️ Hai mangiato la {food}.\n[i]Ti hanno proprio battuto![/i]",
        "diavolo": "👿 Hai mangiato un {food}. Non l'ha presa bene...\n[i]Hai terribili bruciori di stomaco.[/i]",
        "demone": "👿 Hai mangiato un {food}. Non l'ha presa bene...\n[i]Hai terribili bruciori di stomaco.[/i]",
        "niente": "⬜️ Non hai mangiato {food}.\n[i]Hai ancora più fame.[/i]",
        "nulla": "⬜️ Non hai mangiato {food}.\n[i]Hai ancora più fame.[/i]",
        "tre porcellini": "🐷 Hai mangiato i {food}.\n[i]La casa di mattoni non è bastata a fermarti![/i]",
        "3 porcellini": "🐷 Hai mangiato i {food}.\n[i]La casa di mattoni non è bastata a fermarti![/i]",
        "gatto": "🐱 Vieni fermato prima di poter compiere questo gesto orribile.\n"
                 "[i]Il {food} verrà pettato da tutti per farlo riavere dal trauma.[/i]",
        "riso": "🍚 Hai mangiato del {food}. Non ci resta che il Pianto! \n[i]Ba dum tsss![/i]",
        "royal bot": "🤖 Come osi provare a mangiarmi?!\n[i]Il {food} è arrabbiato con te.[/i]",
        "bot": "🤖 Come osi provare a mangiarmi?!\n[i]Il {food} è arrabbiato con te.[/i]",
        "mela": "🍎 Hai mangiato una Mela, e hai fatto bene perché una mela al giorno toglie il medico di torno!\n"
                "[i]Adesso sei molto più sano.[/i]",
        "redbull": "🍾 Hai mangiato {food}.\n[i]Adesso puoi volare![/i]",
        "red bull": "🍾 Hai mangiato {food}.\n[i]Adesso puoi volare![/i]",
        "birra": "🍺 Hai mangiato {food}.\n[i]Adesso sei un povero barbone alcolizzato.[/i]",
        "cacca": "💩 Che schifo! Hai mangiato {food}!\n[i]Allontati per favore, PLEH![/i]",
        "cochina": "🥫 Hai bevuto una {food}. \n[i]Bella fresca.[\i]",
        "little salami" "🥓 Mmmh, tasty!\n[i]Cats can have {food} too![/i]",
        "a little salami" "🥓 Mmmh, tasty!\n[i]Cats can have {food} too![/i]",
        "acqua": "💧 Hai bevuto un po' d'{food}.\n[i]Ti depura e ti fa fare tanta plin plin![/i}",
        "insetto": "🐞 Hai mangiato un {food}.\n[i]Dicono che sia il cibo del futuro, però fa un po' schifo.[/i]",
        "bug": "👾 Bravo, hai mangiato un {food}! Il tuo programma funziona un po' meglio.\n[i] il problema è che"
               "ne sono comparsi altri tre.[/i]",
        "troppo": "⚠️ Hai mangiato {food}!\n[i]Hai un terribile mal di pancia.[/i]",
        "lemon": "🍋 Life gave you {food}s, so you ate them!\n[i]Sono un po' bruschi, ma commestibili.[/i]",
        "lemons": "🍋 Life gave you {food}, so you ate them!\n[i]Sono un po' bruschi, ma commestibili.[/i]",
        "bomba": "💣 Hai mangiato una {food}. Speriamo fosse solo calorica!\n[i]3... 2... 1...[/i]",
        "re": "👑 Hai mangiato il {food} avversario! \n[i]Scacco matto![/i]",
        "cactus": "🌵 Hai mangiato un {food}.\n[i]Gli hai tolto le spine prima, vero?[/i]",
        "kiwi": "🥝 Hai mangiato un {food}!\n[i]Li uoi qvei k-\n Li vuoi kuei uiw- \n Vabbè, avete capito![/i]",
    }

    async def run(self, args: CommandArgs, data: CommandData) -> None:
        food = args.joined(require_at_least=1)
        food_string = self._FOODS.get(food.lower(), self._FOODS["_default"])
        await data.reply(food_string.format(food=food.capitalize()))
