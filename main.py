from kivy.uix.textinput import TextInput
from itertools import chain
from kivy.graphics.texture import Texture
from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager, FadeTransition
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
Window.size = (375, 812)                







class Slope(MDApp):

    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("main.kv"))        
        screen_manager.add_widget(Builder.load_file("signup.kv"))
        screen_manager.add_widget(Builder.load_file("telefoni.kv"))
        screen_manager.add_widget(Builder.load_file("televizori.kv"))        
        screen_manager.add_widget(Builder.load_file("kompjuteri.kv"))
        screen_manager.add_widget(Builder.load_file("mis.kv"))
        screen_manager.add_widget(Builder.load_file("zvucnici.kv"))
        screen_manager.add_widget(Builder.load_file("ostalo.kv"))
        
        
        
        return screen_manager
 #1
    def show_MDDialog(self):
        my_dialog = MDDialog(
                                  
            title="zagrijavanje telefona",
            text = "Prekomjerna upotreba pametnog telefona donosi problem pregrijavanja. Zahtjevne aplikacije, vjerojatnije aplikacije za igranje, povećavaju temperaturu vašeg telefona što može utjecati na performanse baterije. Možda ste preuzeli zlonamjerne aplikacije koje rade u pozadini. Pokušajte ne koristiti telefon dok je napunjen. Nemojte koristiti aplikacije s visokim CPU-om i odmorite svoj telefon. Ako se vaš telefon i dalje grije, to je greška proizvođača.",

            )
        
        my_dialog.open()
        pass
#2    
    def show_MDDialog2(self):
        my_dialog = MDDialog(
            title="Daljinski upravljač ne radi",
            text = "Postoji nekoliko različitih trikova pomoću kojih možete vidjeti je li problem u TV-u ili daljinskom upravljaču. Najprije provjerite ima li daljinski upravljač svježe baterije – to je češće problem kada se čini da je daljinski upravljač pokvaren. Nakon što ste potvrdili da su baterije svježe, možete isprobati mali trik za koji je potreban vaš mobitel: usmjerite kameru telefona na kraj daljinskog upravljača i pritisnite nekoliko tipki. Trebali biste moći vidjeti kako se svjetlo pali kroz kameru. Ako to učinite, problem je TV - pokušajte ga prebaciti na drugu utičnicu i provjerite hoće li to riješiti problem. Ako ne vidite svjetlo, problem je u vašem daljinskom upravljaču. Daljinski upravljači se s vremenom troše, ali možete jednostavno naručiti zamjenu od proizvođača online ili nas kontaktirati kako bismo vam programirali daljinski upravljač po mjeri za vaš sustav.",
        
        
                        )
        my_dialog.open()
        pass

#3
    def show_MDDialog3(self):
        my_dialog = MDDialog(
            title="Blue screen na kompjuteru",
            text = "Ako dobijete plavi zaslon pogreške koja izgleda kao da je povezana s operativnim sustavom ili softverom, možda ćete je moći sami popraviti. Ako kod pogreške koji vidite ima veze s hardverom, ne biste trebali sami pokušavati raditi na računalu jer biste mogli dodatno oštetiti svoje računalo. Kada problemi sa softverom uzrokuju plave ekrane, prvo što biste trebali učiniti je pustiti sustav da se isključi i pokušati se sam ponovno pokrenuti. Moderna računala imaju funkcije i značajke koje će automatski pokušati popraviti ove probleme. Ponekad jednostavno ponovno pokretanje i čekanje može popraviti nasumične plave ekrane. Kada automatski alati ne rade, postoje druga rješenja koja možete pokušati. Možete koristiti alat za instalaciju operativnog sustava da pokušate vratiti ažuriranja ili pokrenuti naprednije alate za popravak bez rizika od daljnjeg oštećenja hardvera. Posljednja stvar koju biste mogli pokušati je ponovno instalirati operativni sustav na računalu. Samo zapamtite da morate biti nevjerojatno oprezni kada to radite jer biste mogli izgubiti sve svoje podatke bez odgovarajućih sigurnosnih kopija.",
        
        
                        )
        my_dialog.open()
        pass
#4
    def show_MDDialog4(self):
        my_dialog = MDDialog(
            title="Miš prestaje da radi",
            text = "Ovaj problem je vrlo rijedak, ali nije bezazlen. Razlog može biti zastarjeli upravljački program koji uzrokuje problem. Morate ponovno instalirati/ažurirati upravljački program miša da biste riješili problem. Također, nemojte preuzimati upravljački program s web-mjesta treće strane. Posjetite web-mjesto proizvođača i preuzmite pravi i najnoviji upravljački program za miš.",
        
        
                        )
        my_dialog.open()
        pass

#5
    def show_MDDialog5(self):
        my_dialog = MDDialog(
            title="Zvučnik ne daje zvuk",
            text = '''Mnogi sustavi zvučnika dolaze sa sigurnosnim okidačima koji ih sprječavaju da ne pucaju preglasno. Vaš uređaj također može spriječiti njegovo previsoko. Provjerite jesu li zvučnici isključeni. Isključeni zvučnici nikada neće proizvoditi zvuk, pa bi vaš popravak mogao biti jednostavan kao uključivanje zvuka problema. Provjerite svoje zvučnike, prijemnik i uređaj koji koristite za reprodukciju zvuka. Sva trojica trebaju biti isključena. Ne zaboravite provjeriti i svoj surround zvuk! Popravite, zamijenite ili spojite sve električne žice. Prema Techwalli, žice su često jedini uzrok bez zvuka. Vaši zvučnici mogu pasti ili popucati ako su spojevi labavi, ali odspojene žice neće moći proizvesti nikakvu buku. Provjerite sve ih kako biste bili sigurni da su dobro priključeni. Pregledajte izlazni uređaj sustava (pametni telefon, prijenosno računalo, TV, sustav za zabavu itd.). Ovi uređaji mogu biti izvor problema jer imaju zasebne tipke za isključivanje zvuka. Prije nego što ih provjerite, smanjite glasnoću zvučnika kako ne bi ispuštali glasnu buku nakon što izvršite potrebne prilagodbe na uređaju. Provjerite jeste li postavili zvučnike na odgovarajući kanal. Neki zvučnici imaju više kanala, stoga je bitno provjeriti jesu li u ispravnom položaju. Ako su vaši zvučnici spojeni na kanal 1, ali prijemnik reproducira zvuk na kanal 2, nećete dobiti nikakav zvuk kroz njih.''',
        
        
                        )
        my_dialog.open()
        pass
#6
    def show_MDDialog6(self):
        my_dialog = MDDialog(
            title="Crveno svjetlo na ps4",
            text = "Ovaj se problem manifestira na sličan način kao kod trepereće plave indikatorske lampice, ali uzroci su različiti. U ovom slučaju, problem je najvjerojatnije zbog pregrijavanja uzrokovanog neispravnim ventilatorom.Evo kako popraviti PS4 konzole s ovim problemom:Isključite svoj PS4 na oko sat vremena da se konzola ohladi.Držite PS4 u dobro prozračenom prostoru, podalje od druge elektronike koja emitira toplinu.Ako nijedan od ovih prijedloga ne uspije, zakažite popravak konzole kako biste popravili ventilator.",
        
        
                        )
        my_dialog.open()
        pass
        



if __name__ == "__main__":
    LabelBase.register(name="futur", fn_regular="futur.ttf")
    LabelBase.register(name="futur2", fn_regular="Futura Heavy font.ttf")
    LabelBase.register(name="futur3", fn_regular="Futura Book font.ttf")

    Slope().run()

