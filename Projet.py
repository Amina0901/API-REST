import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GdkPixbuf

class PagePrincipale(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="PagePrincipale")
        self.set_border_width(100)
        self.set_default_size(300,100)
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#7599CF"))
        self.override_background_color(Gtk.StateFlags.NORMAL, rgba)
  
        grid = Gtk.Grid()
        grid.set_column_spacing(10)
        grid.set_row_spacing(2)
        self.add(grid)

        # frame.set_label("Mon cadre")
        frame = Gtk.Frame()
        frame.set_shadow_type(Gtk.ShadowType.IN) 

        self.add(frame)
        title = Gtk.Label( "**** ROYAL HOTEL **** ")
        title.set_markup("<span size='40200' foreground='#FCFDFD'>{}</span>".format(title.get_text()))
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#2D4365"))
        title.override_background_color(Gtk.StateFlags.NORMAL, rgba)
        grid.attach(title, 0, 0, 2, 1)

        texte_label = Gtk.Label(label="<BIENVENUE AU ROYAL>")
        texte_label.set_markup("<span size='20000' foreground='#092584'>{}</span>".format(texte_label.get_text()))  
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#F9EBD7"))
        texte_label.override_background_color(Gtk.StateFlags.NORMAL, rgba)
        grid.attach(texte_label, 0, 1, 2, 1)

        image = Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file('/Users/famaamar/Documents/ProjetPython/photo2.jpg')
        pixbuf = pixbuf.scale_simple(850, 400, GdkPixbuf.InterpType.BILINEAR)
        image.set_from_pixbuf(pixbuf)
        grid.attach(image, 0, 3, 2, 1)
        
        actionbar = Gtk.ActionBar()
        actionbar.set_hexpand(True)
        grid.attach(actionbar, 0, 4, 2, 1)

        button1 = Gtk.Button("Se connecter")
        actionbar.pack_start(button1)
        actionbar.pack_end(button1)
        button1.connect("clicked", self.connecter)

        button2 = Gtk.Button("Creer Compte")
        actionbar.pack_start(button2)
        actionbar.pack_end(button2)
        button2.connect("clicked", self.inscrire)

    def connecter(self, widget):
        self.hide()
        login_window = LoginPage()
        login_window.show_all()
    def inscrire(self, widget):
        self.hide()
        login_window = Inscription()
        login_window.show_all()    
class Inscription(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="amarIncription")
        self.set_border_width(100)
        self.set_default_size(300,100)
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#7599CF"))
        self.override_background_color(Gtk.StateFlags.NORMAL, rgba)
  
        grid = Gtk.Grid()
        grid.set_column_spacing(10)
        grid.set_row_spacing(2)
        self.add(grid)

        image = Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file('/Users/famaamar/Documents/ProjetPython/photo2.jpg')
        pixbuf = pixbuf.scale_simple(1010, 300, GdkPixbuf.InterpType.BILINEAR)
        image.set_from_pixbuf(pixbuf)
        grid.attach(image, 0, 2, 2, 1)
        #grid.attach(image, 0, 0, 2, 1)
        title = Gtk.Label(" ****INSCRIPTION****")
        title.set_markup("<span size='40200' foreground='#F9EBD7'>{}</span>".format(title.get_text()))
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#2D4365"))
        title.override_background_color(Gtk.StateFlags.NORMAL, rgba)
        grid.attach(title, 0, 0, 2, 1)

        texte_label = Gtk.Label(label="<THE ROYAL,BIENVENUE>")
        texte_label.set_markup("<span size='35000' foreground='#F9EBD7'>{}</span>".format(texte_label.get_text()))  
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#FCFDFD"))
        texte_label.override_background_color(Gtk.StateFlags.NORMAL, rgba)
        grid.attach(texte_label, 0, 1, 2, 1)
        name_label = Gtk.Label(label="Nom:")
        self.tarif = Gtk.Entry()
        name_label.set_markup("<span size='20000' foreground='#092584'>{}</span>".format(name_label.get_text()))  
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#F0ECE5"))
        self.tarif.override_background_color(Gtk.StateFlags.NORMAL, rgba)

        grid.attach(name_label, 0, 3, 1, 1)
        grid.attach(self.tarif, 1, 3, 1, 1)
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#F0ECE5"))
        name_label.override_background_color(Gtk.StateFlags.NORMAL, rgba)

        # Prénom
        firstname_label = Gtk.Label(label="Prénom:")
        self.firstname_entry = Gtk.Entry()
        firstname_label.set_markup("<span size='25000' foreground='#092584'>{}</span>".format(firstname_label.get_text()))  
        grid.attach(firstname_label, 0, 4, 1, 1)
        grid.attach(self.firstname_entry, 1, 4, 1, 1)
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#F0ECE5"))
        self.firstname_entry.override_background_color(Gtk.StateFlags.NORMAL, rgba)
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#F0ECE5"))
        firstname_label.override_background_color(Gtk.StateFlags.NORMAL, rgba)

        # E-mail
        email_label = Gtk.Label(label="Adresse E-mail:")
        self.email_entry = Gtk.Entry()
        email_label.set_markup("<span size='25000' foreground='#092584'>{}</span>".format(email_label.get_text()))  
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#F0ECE5"))
        self.email_entry.override_background_color(Gtk.StateFlags.NORMAL, rgba)
        grid.attach(email_label, 0, 5, 1, 1)
        grid.attach(self.email_entry, 1, 5, 1, 1)
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#F0ECE5"))
        email_label.override_background_color(Gtk.StateFlags.NORMAL, rgba)

        # Mot de passe
        password_label = Gtk.Label(label="Mot de passe:")
        self.password_entry = Gtk.Entry()
        password_label.set_markup("<span size='25000' foreground='#092584'>{}</span>".format(password_label.get_text()))  
        self.password_entry.set_visibility(False)
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#F0ECE5"))
        self.password_entry.override_background_color(Gtk.StateFlags.NORMAL, rgba)
        grid.attach(password_label, 0, 6, 1, 1)
        grid.attach(self.password_entry, 1, 6, 1, 1)
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#F0ECE5"))
        password_label.override_background_color(Gtk.StateFlags.NORMAL, rgba)

        # Bouton d'inscription
        register_button = Gtk.Button(label="S'inscrire")
        register_button.connect("clicked", self.inscrire)
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#F0ECE5"))
        register_button.override_background_color(Gtk.StateFlags.NORMAL, rgba)
        grid.attach(register_button, 1, 7, 1, 1)

          # Bouton de retour
        retour_button = Gtk.Button(label="Retour")
        retour_button.connect("clicked", self.retourner)
        grid.attach(retour_button, 0, 7, 1, 1)

    def retourner(self, widget):
            self.hide()
            login_window = PagePrincipale()
            login_window.show_all()

    def inscrire(self, widget):
        self.hide()
        login_window = LoginPage()
        login_window.show_all()
class LoginPage(Gtk.Window):
    def __init__(self): 
        Gtk.Window.__init__(self, title="Page D'accueil")
        self.set_border_width(100)
        self.set_default_size(300,100)
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#7599CF"))
        self.override_background_color(Gtk.StateFlags.NORMAL, rgba)
  
        grid = Gtk.Grid()
        grid.set_column_spacing(10)
        grid.set_row_spacing(2)
        self.add(grid)

        image = Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file('/Users/famaamar/Documents/ProjetPython/photo2.jpg')
        pixbuf = pixbuf.scale_simple(1010, 300, GdkPixbuf.InterpType.BILINEAR)
        image.set_from_pixbuf(pixbuf)
        grid.attach(image, 0, 2, 2, 1)
        #grid.attach(image, 0, 0, 2, 1)
        title = Gtk.Label(" ****CONNEXION**** ")
        title.set_markup("<span size='40200' foreground='#F9EBD7'>{}</span>".format(title.get_text()))
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#2D4365"))
        title.override_background_color(Gtk.StateFlags.NORMAL, rgba)
        grid.attach(title, 0, 0, 2, 1)

        texte_label = Gtk.Label(label="<THE ROYAL,BIENVENUE>")
        texte_label.set_markup("<span size='35000' foreground='#F9EBD7'>{}</span>".format(texte_label.get_text()))  
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#FCFDFD"))
        texte_label.override_background_color(Gtk.StateFlags.NORMAL, rgba)
        grid.attach(texte_label, 0, 1, 2, 1)

         # E_mail
        email_label = Gtk.Label(label="Adresse E-mail:")
        grid.attach(email_label, 0, 3, 1, 1)
        self.email_entry = Gtk.Entry()
        email_label.set_markup("<span size='25000' foreground='#F9EBD7'>{}</span>".format(email_label.get_text()))  
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#F0ECE5"))
        self.email_entry.override_background_color(Gtk.StateFlags.NORMAL, rgba)
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#F8E9D2"))
        email_label.override_background_color(Gtk.StateFlags.NORMAL, rgba)

        # Entrée Email
        self.mail = Gtk.Entry()
        grid.attach(self.mail, 1, 3, 1, 1)
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#F8E9D2"))
        self.mail.override_background_color(Gtk.StateFlags.NORMAL, rgba)

       # password
        password = Gtk.Label(label="Mot de Passe")
        grid.attach(password, 0, 4, 1, 1)
        password.set_markup("<span size='20000' foreground='#092584'>{}</span>".format(password.get_text()))  
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#F8E9D2"))
        password.override_background_color(Gtk.StateFlags.NORMAL, rgba)
        password.set_size_request(20, 10)
        # Entrée passwor
        self.password_entry = Gtk.Entry()
        grid.attach(self.password_entry, 1, 4, 1, 1)
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#F8E9D2"))
        self.password_entry.override_background_color(Gtk.StateFlags.NORMAL, rgba)
        self.password_entry.set_visibility(False)

        # Bouton de connexion
        connect_button = Gtk.Button(label="Se connecter")
        connect_button.connect("clicked", self.on_connect_clicked)
        connect_button.set_size_request(20, 10) 
        grid.attach(connect_button, 0, 5, 2, 2)

         # Bouton de retour
        retour_button = Gtk.Button(label="Retour")
        retour_button.connect("clicked", self.on_retour_clicked)
        retour_button.set_size_request(20, 10) 
        grid.attach(retour_button, 0, 7, 2, 2)
        # Code pour valider le retour
    def on_retour_clicked(self, widget):
            self.hide()
            login_window = PagePrincipale()
            login_window.show_all()
         # Code pour valider la connexion
    def on_connect_clicked(self, widget):
        self.hide()
        login_window = PageAccueil()
        login_window.show_all()  
class PageAccueil(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Page D'accueil")
        self.set_border_width(100)
        self.set_default_size(800,200)
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#7599CF"))
        self.override_background_color(Gtk.StateFlags.NORMAL, rgba)
  
        grid = Gtk.Grid()
        grid.set_column_spacing(10)
        grid.set_row_spacing(2)
        self.add(grid)

        image = Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file('/Users/famaamar/Documents/ProjetPython/photo2.jpg')
        pixbuf = pixbuf.scale_simple(800, 300, GdkPixbuf.InterpType.BILINEAR)
        image.set_from_pixbuf(pixbuf)
        grid.attach(image, 0, 3, 2, 1)

        #grid.attach(image, 0, 0, 2, 1)
        title = Gtk.Label("****ACCUEIL**** ")
        title.set_markup("<span size='40200' foreground='#F9EBD7'>{}</span>".format(title.get_text()))
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#2D4365"))
        title.override_background_color(Gtk.StateFlags.NORMAL, rgba)
        grid.attach(title, 0, 0, 2, 1)

        texte_label = Gtk.Label(label="<THE ROYAL,BIENVENUE>")
        texte_label.set_markup("<span size='35000' foreground='#F9EBD7'>{}</span>".format(texte_label.get_text()))  
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#FCFDFD"))
        texte_label.override_background_color(Gtk.StateFlags.NORMAL, rgba)
        grid.attach(texte_label, 0, 1, 2, 1)

        # Menu avec les options de réservation, clients et chambres
        menu_bar = Gtk.MenuBar()
        #menu_bar.set_size_request(100, 50)
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#F0CDAD"))
        menu_bar.override_background_color(Gtk.StateFlags.NORMAL, rgba)
        grid.attach(menu_bar, 0, 2, 2, 1)

        hotel_menu = Gtk.Menu()
        hotel_menu_item = Gtk.MenuItem(label="Informations")
        hotel_menu_item.set_submenu(hotel_menu)
        menu_bar.append(hotel_menu_item)

        reservation_menu = Gtk.Menu()
        reservation_menu_item = Gtk.MenuItem(label="Réservations")
        reservation_menu_item.set_submenu(reservation_menu)
        menu_bar.append(reservation_menu_item)

        client_menu = Gtk.Menu()
        client_menu_item = Gtk.MenuItem(label="Clients")
        client_menu_item.set_submenu(client_menu)
        menu_bar.append(client_menu_item)

        chambre_menu = Gtk.Menu()
        chambre_menu_item = Gtk.MenuItem(label="Chambres")
        chambre_menu_item.set_submenu(chambre_menu)
        menu_bar.append(chambre_menu_item)

        facture_menu = Gtk.Menu()
        facture_menu_item = Gtk.MenuItem(label=" factures")
        facture_menu_item.set_submenu( facture_menu)
        menu_bar.append(facture_menu_item)

        statistiques_menu = Gtk.Menu()
        statistiques_menu_item = Gtk.MenuItem(label=" statistiquess")
        statistiques_menu_item.set_submenu( statistiques_menu)
        menu_bar.append(statistiques_menu_item)

        quitter_menu_item = Gtk.Menu()
        quitter_menu_item = Gtk.MenuItem(label=" quitter")
        quitter_menu_item.connect("activate", self.quitter_menu)
        menu_bar.append(quitter_menu_item)

        # Options du menu Réservations
        voir_info = Gtk.MenuItem(label="Voir infos")
        voir_info.connect("activate", self.voir_info)
        hotel_menu.append(voir_info)

        ajouter_reservation = Gtk.MenuItem(label="Ajouter réservation")
        ajouter_reservation.connect("activate", self.ajouter_reservation)
        reservation_menu.append(ajouter_reservation)

        consulter_reservations = Gtk.MenuItem(label="Consulter les réservations")
        consulter_reservations.connect("activate", self.consulter_reservations)
        reservation_menu.append(consulter_reservations)

        supprimer_reservation = Gtk.MenuItem(label="Supprimer")
        supprimer_reservation.connect("activate", self.supprimer_reservation )
        reservation_menu.append(supprimer_reservation)
        # Options du menu Clients
        nouveau_client = Gtk.MenuItem(label="Ajouter client")
        nouveau_client.connect("activate", self.nouveau_client)
        client_menu.append(nouveau_client)

        lister_Clients = Gtk.MenuItem(label="Lister les clients")
        lister_Clients.connect("activate", self.lister_Clients)
        client_menu.append(lister_Clients)

        # Options du menu Chambres
        nouvelle_chambre = Gtk.MenuItem(label="Nouvelle chambre")
        nouvelle_chambre.connect("activate", self.nouvelle_chambre)
        chambre_menu.append(nouvelle_chambre)

        lister_chambres = Gtk.MenuItem(label="liste des chambres")
        lister_chambres.connect("activate", self.lister_chambres)
        chambre_menu.append(lister_chambres)

        # Options du menu factures
        nouvelle_facture = Gtk.MenuItem(label="Facturer")
        nouvelle_facture.connect("activate", self.nouvelle_facture)
        facture_menu.append(nouvelle_facture)

        consulter_factures = Gtk.MenuItem(label="Consulter les factures")
        consulter_factures.connect("activate", self.consulter_factures)
        facture_menu.append(consulter_factures)

         # Options du menu statistiquess
        Statistiques = Gtk.MenuItem(label="Nouvelle statistiques")
        Statistiques.connect("activate", self.Statistiques)
        statistiques_menu.append(Statistiques)
        
    #Definition des fonctions
    def ajouter_reservation(self, widget):
        self.hide()
        login_window = PageReservation()
        login_window.show_all()
        print("reservation effectuer")
    
    def nouveau_client (self, widget):
       self.hide()
       login_window = AjoutClients()
       login_window.show_all()
    print("")

    def lister_Clients(self, widget):
         self.hide()
         win = PageListerClients()
         win.show_all()

    def voir_info(self, widget):
         self.hide()
         win = PageListerClients()
         win.show_all()
    
    def quitter_menu(self, widget):
         self.hide()
         win = PagePrincipale()
         win.show_all()
      
    def lister_chambres(self, widget):
      self.hide()
      win = ListerChambre()
      win.show_all()
    print("")

    def consulter_reservations(self, widget):
        """ self.hide()
      login_window = AjoutChambres()
      login_window.show_all()"""
        print("")

    def supprimer_reservation(self, widget):
        """ self.hide()
      login_window = AjoutChambres()
      login_window.show_all()"""
        print("")

    def nouvelle_chambre(self, widget):
      self.hide()
      login_window = AjoutChambre()
      login_window.show_all()
    print("")
  
    def nouvelle_facture(self, widget):
        """ self.hide()
      login_window = AjoutChambres()
      login_window.show_all()"""
        print("")

    def consulter_factures(self, widget):
        """ self.hide()
      login_window = AjoutChambres()
      login_window.show_all()"""  
        print("")

    def Statistiques(self, widget):
        """ self.hide()
      login_window = AjoutChambres()
      login_window.show_all()""" 
        print("")
class PageReservation(Gtk.Window):
     def __init__(self):
        Gtk.Window.__init__(self, title="Formulaire  Reservation")
        self.set_border_width(100)
        self.set_default_size(800,400)
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#7599CF"))
        self.override_background_color(Gtk.StateFlags.NORMAL, rgba)
  
        grid = Gtk.Grid()
        grid.set_column_spacing(10)
        grid.set_row_spacing(2)
        self.add(grid)

        title = Gtk.Label("****RESERVATION**** ")
        title.set_markup("<span size='40200' foreground='#F9EBD7'>{}</span>".format(title.get_text()))
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#2D4365"))
        title.override_background_color(Gtk.StateFlags.NORMAL, rgba)
        grid.attach(title, 0, 0, 2, 1)

        texte_label = Gtk.Label(label="<THE ROYAL,BIENVENUE>")
        texte_label.set_markup("<span size='35000' foreground='#092584'>{}</span>".format(texte_label.get_text()))  
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#F9EBD7"))
        texte_label.override_background_color(Gtk.StateFlags.NORMAL, rgba)
        grid.attach(texte_label, 0, 1, 2, 1)

        image = Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file('/Users/famaamar/Documents/ProjetPython/photo2.jpg')
        pixbuf = pixbuf.scale_simple(700, 300, GdkPixbuf.InterpType.BILINEAR)
        image.set_from_pixbuf(pixbuf)
        grid.attach(image, 0, 2, 2, 1)

        label1  = Gtk.Label(label="Date d'arrivée::")
        self.arrivé = Gtk.Entry()
        label1.set_markup("<span size='20000' foreground='#092584'>{}</span>".format( label1.get_text()))  
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#F9EBD7"))
        self.arrivé.override_background_color(Gtk.StateFlags.NORMAL, rgba)

        grid.attach( label1 , 0, 3, 1, 1)
        grid.attach(self.arrivé, 1, 3, 1, 1)
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#F9EBD7"))
        label1 .override_background_color(Gtk.StateFlags.NORMAL, rgba)

         # date de départ
        label2 = Gtk.Label(label="Date départ::")
        self.depart = Gtk.Entry()
        label2.set_markup("<span size='20000' foreground='#092584'>{}</span>".format( label2.get_text()))  
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#F9EBD7"))
        self.depart.override_background_color(Gtk.StateFlags.NORMAL, rgba)

        grid.attach( label2, 0, 4, 1, 1)
        grid.attach(self.depart, 1, 4, 1, 1)
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#F9EBD7"))
        label2.override_background_color(Gtk.StateFlags.NORMAL, rgba)

        #   tarif
        label3 = Gtk.Label(label="Tarif (en Fcfa):")
        self.tarif = Gtk.Entry()
        label3.set_markup("<span size='20000' foreground='#092584'>{}</span>".format(label3.get_text()))  
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#F9EBD7"))
        self.tarif.override_background_color(Gtk.StateFlags.NORMAL, rgba)
        
        grid.attach(label3, 0, 5, 1, 1)
        grid.attach(self.tarif, 1, 5, 1, 1)
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#F9EBD7"))
        label3.override_background_color(Gtk.StateFlags.NORMAL, rgba)

         #   nombre de nuitées

        label4 = Gtk.Label(label="Nombre de nuitées:")
        self.nuitée = Gtk.Entry()
        label4.set_markup("<span size='20000' foreground='#092584'>{}</span>".format(label4.get_text()))  
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#F9EBD7"))
        self.nuitée.override_background_color(Gtk.StateFlags.NORMAL, rgba)

        grid.attach(label4, 0, 6, 1, 1)
        grid.attach(self.nuitée, 1, 6, 1, 1)
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#F9EBD7"))
        label4.override_background_color(Gtk.StateFlags.NORMAL, rgba)

         # bouton pour valider la réservation
        button = Gtk.Button(label="Reserver")
        button.connect("clicked", self.tapeReserver)
        grid.attach(button, 0, 7, 2, 1)

        # Bouton de retour
        retour_button = Gtk.Button(label="Retour")
        retour_button.connect("clicked", self.retourner)
        retour_button.set_size_request(20, 10) 
        grid.attach(retour_button, 0, 8, 2, 1)

     def tapeResever(self, widget):
        self.hide()
        login_window = PageAccueil()
        login_window.show_all()
     
        # Code pour valider le retour
     def retourner(self, widget):
            self.hide()
            login_window = PageAccueil()
            login_window.show_all()    

     def tapeReserver(self, widget):
          # Récupérer les données du formulaire et les afficher
        date_arrivee = self.date_arrivee.get_text()
        date_depart = self.date_depart.get_text()
        tarif = self.tarif.get_text()
        nuitees = self.nuitees.get_text()

        self.print("Date d'arrivée : ", date_arrivee)
        self.print("Date de départ : ", date_depart)
        self.print("Tarif : ", tarif)
        self.print("Nombre de nuitées : ", nuitees)
class PageConsulterResevation(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Formulaire  Reservation")
        self.set_border_width(10)
        grid = Gtk.Grid()
        grid.set_column_spacing(10)
        grid.set_row_spacing(10)
        self.add(grid)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=1)
        image = Gtk.Image.new_from_file("/Users/famaamar/Documents/ProjetPython/hotel.jpeg")
        box.pack_start(image, False, False, 0)

        label = Gtk.Label("****AJOUTER RESERVATION****")
        label.set_markup("<span size='20000' foreground='black'>{}</span>".format(label.get_text()))
        label.set_size_request(10, 5)
        box.pack_start(label, False, False, 0)
        box.set_size_request(10, 5)
        grid.attach(box, 1, 0, 1, 1)
        grid.add(label)


         # Récupérer les données du formulaire et les afficher
        date_arrivee = self.date_arrivee.get_text()
        date_depart = self.date_depart.get_text()
        tarif = self.tarif.get_text()
        nuitees = self.nuitees.get_text()

        self.print("Date d'arrivée : ", date_arrivee)
        self.print("Date de départ : ", date_depart)
        self.print("Tarif : ", tarif)
        self.print("Nombre de nuitées : ", nuitees)
        
        date_arrivee = Gtk.Label( self.print("Date d'arrivée : ", date_arrivee),label="Nombre de nuitées:")
        grid.attach(self.date_arrivee , 1, 4, 1, 1)
        date_depart = Gtk.Label(self.date_depart.get_text(),label="Nombre de nuitées:")
        grid.attach(self.date_depart , 1, 4, 1, 1)
        tarif = Gtk.Label(self.tarif.get_text(),label="Nombre de nuitées:")
        grid.attach(self.tarif , 1, 4, 1, 1)
        nuitees= Gtk.Label(self.nuitees.get_text(),label="Nombre de nuitées:")
        grid.attach(self.nuitees, 1, 4, 1, 1)
class AjoutClients(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="amarAjout")
        self.set_border_width(100)
        self.set_default_size(800,400)
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#7599CF"))
        self.override_background_color(Gtk.StateFlags.NORMAL, rgba)
  
        grid = Gtk.Grid()
        grid.set_column_spacing(10)
        grid.set_row_spacing(2)
        self.add(grid)

        title = Gtk.Label("****AJOUTER CLIENT**** ")
        title.set_markup("<span size='40200' foreground='#F9EBD7'>{}</span>".format(title.get_text()))
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#2D4365"))
        title.override_background_color(Gtk.StateFlags.NORMAL, rgba)
        grid.attach(title, 1, 0, 2, 1)

        texte_label = Gtk.Label(label="<THE ROYAL,BIENVENUE>")
        texte_label.set_markup("<span size='35000' foreground='#092584'>{}</span>".format(texte_label.get_text()))  
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#FCFDFD"))
        texte_label.override_background_color(Gtk.StateFlags.NORMAL, rgba)
        grid.attach(texte_label, 1, 1, 2, 1)

        image = Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file('/Users/famaamar/Documents/ProjetPython/photo2.jpg')
        pixbuf = pixbuf.scale_simple(800, 350, GdkPixbuf.InterpType.BILINEAR)
        image.set_from_pixbuf(pixbuf)
        grid.attach(image, 1, 2, 2, 1)

        # Création d'un widget de cadre pour encadrer le tableau
        cadre = Gtk.Frame()
        grid.attach(cadre, 2, 3, 1, 1)

        tableau = Gtk.Grid()
        cadre.add(tableau)
        cadre.set_border_width(20)
        tableau.set_column_spacing(5)
        tableau.set_row_spacing(2)

        # Numero
        label1 = Gtk.Label(label="Telephone:")
        tableau.attach(label1, 0, 1, 1, 1)
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#F8E9D2"))
        label1.override_background_color(Gtk.StateFlags.NORMAL, rgba)
        label1.set_markup("<span size='20000' foreground='#092584'>{}</span>".format(label1.get_text()))  

        # Entre Numero
        self.numero = Gtk.Entry()
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#F8E9D2"))
        self.numero.override_background_color(Gtk.StateFlags.NORMAL, rgba)
        tableau.attach(self.numero, 1, 1, 1, 1)


        # Prenom
        label2 = Gtk.Label(label="Prenom:")
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#F8E9D2"))
        label2.override_background_color(Gtk.StateFlags.NORMAL, rgba)
        label2.set_markup("<span size='20000' foreground='#092584'>{}</span>".format(label2.get_text()))  
        tableau.attach(label2, 0, 2, 1, 1)

        # 
        self.prenom = Gtk.Entry()
        tableau.attach(self.prenom, 1, 2, 1, 1)
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#F8E9D2"))
        self.prenom.override_background_color(Gtk.StateFlags.NORMAL, rgba)

        # Nom
        label3 = Gtk.Label(label="Nom:")
        tableau.attach(label3, 0, 3, 1, 1)
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#F8E9D2"))
        label3.override_background_color(Gtk.StateFlags.NORMAL, rgba)
        label3.set_markup("<span size='20000' foreground='#092584'>{}</span>".format(label3.get_text()))  


        # 
        self.nom = Gtk.Entry()
        tableau.attach(self.nom, 1, 3, 1, 1)
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#F8E9D2"))
        self.nom.override_background_color(Gtk.StateFlags.NORMAL, rgba)


        # IdResevation
        label4 = Gtk.Label(label="IdResevation")
        tableau.attach(label4, 0, 4, 1, 1)
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#F8E9D2"))
        label4.override_background_color(Gtk.StateFlags.NORMAL, rgba)
        label4.set_markup("<span size='20000' foreground='#092584'>{}</span>".format(label4.get_text()))  


        # 
        self.id = Gtk.Entry()
        tableau.attach(self.id, 1, 4, 1, 1)
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#F8E9D2"))
        self.id.override_background_color(Gtk.StateFlags.NORMAL, rgba)

        # bouton
        button = Gtk.Button(label="Ajouter")
        button.connect("clicked", self.AjouterClients)
        tableau.attach(button, 0, 5, 1, 1)

          # Bouton de retour
        retour_button = Gtk.Button(label="Retour")
        retour_button.connect("clicked", self.retourner)
        tableau.attach(retour_button, 1, 5, 1, 1)

    def retourner(self, widget):
            self.hide()
            login_window = PageAccueil()
            login_window.show_all()
        
    def AjouterClients (self, widget):
          # Récupérer les données du formulaire et les afficher
        numero = self.numero.get_text()
        prenom = self.prenom.get_text()
        nom = self.nom.get_text()
        id = self.id.get_text()

        self.print(" : ", numero)
        self.print("Prenom : ", prenom)
        self.print("Nom : ", nom)
        self.print("IdReservation : ",id)        
class PageListerClients(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Lister Clients")
        self.set_border_width(100)
        self.set_default_size(800,200)
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#7599CF"))
        self.override_background_color(Gtk.StateFlags.NORMAL, rgba)
  
        grid = Gtk.Grid()
        grid.set_column_spacing(5)
        grid.set_row_spacing(2)
        self.add(grid)

        # frame.set_label("Mon cadre")
        frame = Gtk.Frame()
        frame.set_shadow_type(Gtk.ShadowType.IN) 

        self.add(frame)
        title = Gtk.Label( "**** LISTE CLIENTS **** ")
        title.set_markup("<span size='40200' foreground='#FCFDFD'>{}</span>".format(title.get_text()))
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#2D4365"))
        title.override_background_color(Gtk.StateFlags.NORMAL, rgba)
        grid.attach(title, 2, 0, 2, 1)

        texte_label = Gtk.Label(label="<THE ROYAL,BIENVENUE>")
        texte_label.set_markup("<span size='35000' foreground='#092584'>{}</span>".format(texte_label.get_text()))  
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#FCFDFD"))
        texte_label.override_background_color(Gtk.StateFlags.NORMAL, rgba)
        grid.attach(texte_label, 2, 1, 2, 1)

        image = Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file('/Users/famaamar/Documents/ProjetPython/photo2.jpg')
        pixbuf = pixbuf.scale_simple(700, 350, GdkPixbuf.InterpType.BILINEAR)
        image.set_from_pixbuf(pixbuf)
        grid.attach(image, 2, 2, 2, 1)

        # Création du tableau

        class Client:
            def __init__(self,prenom, nom,telephone ,id ):
                
                self.prenom = prenom
                self.nom = nom
                self.telephone = telephone
                self.id = id
        clients =[Client("fama","Amar", "783080350", "01AA"),
                  
                    Client("Aminata","Diop", "774003002", "02AD"),

                    Client("Lamine", "Ka", "773457533", "03LK"),

                    Client("Ibrahima", "Diarra", "775637837", "04ID")]
    
          
        cadre = Gtk.Frame()
        cadre.set_border_width(20)
        grid.attach(cadre, 2, 3, 1, 1)

        tableau = Gtk.Grid()
        cadre.add(tableau)
        tableau.set_column_spacing(20)
        tableau.set_row_spacing(20)
       
        prenom_label = Gtk.Label("Prénom")
        prenom_label.set_markup("<span size='20000' foreground='#092584'>{}</span>".format(prenom_label.get_text()))  
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#FCFDFD"))
        prenom_label.override_background_color(Gtk.StateFlags.NORMAL, rgba)
        tableau.attach(prenom_label, 0, 0, 1, 1)

        nom_label = Gtk.Label("Nom")
        nom_label.set_markup("<span size='20000' foreground='#092584'>{}</span>".format(nom_label.get_text()))  
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#FCFDFD"))
        nom_label.override_background_color(Gtk.StateFlags.NORMAL, rgba)
        tableau.attach(nom_label, 1, 0, 1, 1)

        id_label = Gtk.Label("NumReservation")
        tableau.attach(id_label, 2, 0, 1, 1)
        id_label.set_markup("<span size='20000' foreground='#092584'>{}</span>".format(id_label.get_text()))  
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#FCFDFD"))
        id_label.override_background_color(Gtk.StateFlags.NORMAL, rgba)

        telephone_label = Gtk.Label("Téléphone")
        tableau.attach(telephone_label, 3, 0, 1, 1)
        telephone_label.set_markup("<span size='22000' foreground='#092584'>{}</span>".format(telephone_label.get_text()))  
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#FCFDFD"))
        telephone_label.override_background_color(Gtk.StateFlags.NORMAL, rgba)

            # Ajout des clients dans le tableau
        for i, client in enumerate(clients):
                prenom_label = Gtk.Label(client.prenom)
                prenom_label.set_markup("<span size='20000' foreground='#092584'>{}</span>".format(prenom_label.get_text()))  
                tableau.attach(prenom_label, 0, i+1, 1, 1)

                nom_label = Gtk.Label(client.nom)
                nom_label.set_markup("<span size='20000' foreground='#092584'>{}</span>".format(nom_label.get_text()))  
                tableau.attach(nom_label, 1, i+1, 1, 1)

                id_label = Gtk.Label(client.id)
                id_label.set_markup("<span size='20000' foreground='#092584'>{}</span>".format(id_label.get_text()))  
                tableau.attach(id_label, 2, i+1, 1, 1)
                
                telephone_label = Gtk.Label(client.telephone)
                telephone_label.set_markup("<span size='20000' foreground='#092584'>{}</span>".format(telephone_label.get_text()))  
                tableau.attach(telephone_label, 3, i+1, 1, 1)


                 # Bouton de retour
         
        actionbar = Gtk.ActionBar()
        actionbar.set_hexpand(True)
        tableau.attach(actionbar, 1, 5, 2, 1)

        button1 = Gtk.Button("Retour")
        actionbar.pack_start(button1)
        actionbar.pack_end(button1)
        button1.connect("clicked", self.retourner)
    
    def retourner(self, widget):
        self.hide()
        login_window = PageAccueil()
        login_window.show_all()
class AjoutChambre(Gtk.Window):
     def __init__(self):
        Gtk.Window.__init__(self, title="_AMARY_HOTEL")
        self.set_border_width(100)
        self.set_default_size(800,400)
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#7599CF"))
        self.override_background_color(Gtk.StateFlags.NORMAL, rgba)
  
        grid = Gtk.Grid()
        grid.set_column_spacing(10)
        grid.set_row_spacing(2)
        self.add(grid)

        title = Gtk.Label("****AJOUTER CHAMBRE**** ")
        title.set_markup("<span size='40200' foreground='#F9EBD7'>{}</span>".format(title.get_text()))
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#2D4365"))
        title.override_background_color(Gtk.StateFlags.NORMAL, rgba)
        grid.attach(title, 1, 0, 2, 1)

        texte_label = Gtk.Label(label="<THE ROYAL,BIENVENUE>")
        texte_label.set_markup("<span size='35000' foreground='#092584'>{}</span>".format(texte_label.get_text()))  
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#F9EBD7"))
        texte_label.override_background_color(Gtk.StateFlags.NORMAL, rgba)
        grid.attach(texte_label, 1, 1, 2, 1)

        image = Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file('/Users/famaamar/Documents/ProjetPython/chambre.jpg')
        pixbuf = pixbuf.scale_simple(800, 350, GdkPixbuf.InterpType.BILINEAR)
        image.set_from_pixbuf(pixbuf)
        grid.attach(image, 1, 2, 2, 1)

        # Création d'un widget de cadre pour encadrer le tableau
        cadre = Gtk.Frame()
        grid.attach(cadre, 2, 3, 1, 1)

        tableau = Gtk.Grid()
        cadre.add(tableau)
        cadre.set_border_width(20)
        tableau.set_column_spacing(5)
        tableau.set_row_spacing(2)

        # Numero
        label1 = Gtk.Label(label="Numero Niveau:")
        tableau.attach(label1, 0, 1, 1, 1)
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#F9EBD7"))
        label1.override_background_color(Gtk.StateFlags.NORMAL, rgba)
        label1.set_markup("<span size='20000' foreground='#092584'>{}</span>".format(label1.get_text()))  

        # Entre Numero
        self.numero = Gtk.Entry()
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#F8E9D2"))
        self.numero.override_background_color(Gtk.StateFlags.NORMAL, rgba)
        tableau.attach(self.numero, 1, 1, 1, 1)


        # Prenom
        label2 = Gtk.Label(label="Classe:")
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#F9EBD7"))
        label2.override_background_color(Gtk.StateFlags.NORMAL, rgba)
        label2.set_markup("<span size='20000' foreground='#092584'>{}</span>".format(label2.get_text()))  
        tableau.attach(label2, 0, 2, 1, 1)

        # 
        self.prenom = Gtk.Entry()
        tableau.attach(self.prenom, 1, 2, 1, 1)
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#F8E9D2"))
        self.prenom.override_background_color(Gtk.StateFlags.NORMAL, rgba)

        # Nom
        label3 = Gtk.Label(label="Nom Chambre:")
        tableau.attach(label3, 0, 3, 1, 1)
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#F9EBD7"))
        label3.override_background_color(Gtk.StateFlags.NORMAL, rgba)
        label3.set_markup("<span size='20000' foreground='#092584'>{}</span>".format(label3.get_text()))  


        # 
        self.nom = Gtk.Entry()
        tableau.attach(self.nom, 1, 3, 1, 1)
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#F8E9D2"))
        self.nom.override_background_color(Gtk.StateFlags.NORMAL, rgba)


        # IdResevation
        label4 = Gtk.Label(label="Etat de la chambre")
        tableau.attach(label4, 0, 4, 1, 1)
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#F9EBD7"))
        label4.override_background_color(Gtk.StateFlags.NORMAL, rgba)
        label4.set_markup("<span size='20000' foreground='#092584'>{}</span>".format(label4.get_text()))  


        # 
        self.id = Gtk.Entry()
        tableau.attach(self.id, 1, 4, 1, 1)
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#F8E9D2"))
        self.id.override_background_color(Gtk.StateFlags.NORMAL, rgba)

        # bouton
        button = Gtk.Button(label="Ajouter")
        button.connect("clicked", self.AjouterChambre)
        tableau.attach(button, 0, 5, 1, 1)

          # Bouton de retour
        retour_button = Gtk.Button(label="Retour")
        retour_button.connect("clicked", self.retourner)
        tableau.attach(retour_button, 1, 5, 1, 1)

     def retourner(self, widget):
            self.hide()
            login_window = PageAccueil()
            login_window.show_all()
     def AjouterChambre(self, widget):
            self.hide()
            login_window = PageAccueil()
            login_window.show_all()
class ListerChambre (Gtk.Window):
     def __init__(self):
        Gtk.Window.__init__(self, title="Lister Clients")
        self.set_border_width(100)
        self.set_default_size(800,200)
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#7599CF"))
        self.override_background_color(Gtk.StateFlags.NORMAL, rgba)
  
        grid = Gtk.Grid()
        grid.set_column_spacing(5)
        grid.set_row_spacing(2)
        self.add(grid)

        # frame.set_label("Mon cadre")
        frame = Gtk.Frame()
        frame.set_shadow_type(Gtk.ShadowType.IN) 

        self.add(frame)
        title = Gtk.Label( "**** LISTE CHAMBRES **** ")
        title.set_markup("<span size='40200' foreground='#FCFDFD'>{}</span>".format(title.get_text()))
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#2D4365"))
        title.override_background_color(Gtk.StateFlags.NORMAL, rgba)
        grid.attach(title, 2, 0, 2, 1)

        texte_label = Gtk.Label(label="<THE ROYAL,BIENVENUE>")
        texte_label.set_markup("<span size='35000' foreground='#092584'>{}</span>".format(texte_label.get_text()))  
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#FCFDFD"))
        texte_label.override_background_color(Gtk.StateFlags.NORMAL, rgba)
        grid.attach(texte_label, 2, 1, 2, 1)

        image = Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file('/Users/famaamar/Documents/ProjetPython/photo2.jpg')
        pixbuf = pixbuf.scale_simple(700, 350, GdkPixbuf.InterpType.BILINEAR)
        image.set_from_pixbuf(pixbuf)
        grid.attach(image, 2, 2, 2, 1)

        # Création du tableau

        class Client:
            def __init__(self,prenom, nom,telephone ,id ):
                
                self.prenom = prenom
                self.nom = nom
                self.telephone = telephone
                self.id = id
        clients =[Client("Chambre1","00", "classe1", "Occuper"),
                  
                    Client("Chambre2","01", "Classe2", "Liberer"),

                   ]
    
          
        cadre = Gtk.Frame()
        cadre.set_border_width(20)
        grid.attach(cadre, 2, 3, 1, 1)

        tableau = Gtk.Grid()
        cadre.add(tableau)
        tableau.set_column_spacing(20)
        tableau.set_row_spacing(20)
       
        prenom_label = Gtk.Label("Nom Chambre")
        prenom_label.set_markup("<span size='20000' foreground='#092584'>{}</span>".format(prenom_label.get_text()))  
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#FCFDFD"))
        prenom_label.override_background_color(Gtk.StateFlags.NORMAL, rgba)
        tableau.attach(prenom_label, 0, 0, 1, 1)

        nom_label = Gtk.Label("Numero Niveau")
        nom_label.set_markup("<span size='20000' foreground='#092584'>{}</span>".format(nom_label.get_text()))  
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#FCFDFD"))
        nom_label.override_background_color(Gtk.StateFlags.NORMAL, rgba)
        tableau.attach(nom_label, 1, 0, 1, 1)

        id_label = Gtk.Label("Etat Chambre")
        tableau.attach(id_label, 2, 0, 1, 1)
        id_label.set_markup("<span size='20000' foreground='#092584'>{}</span>".format(id_label.get_text()))  
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#FCFDFD"))
        id_label.override_background_color(Gtk.StateFlags.NORMAL, rgba)

        telephone_label = Gtk.Label("Classe")
        tableau.attach(telephone_label, 3, 0, 1, 1)
        telephone_label.set_markup("<span size='22000' foreground='#092584'>{}</span>".format(telephone_label.get_text()))  
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("#FCFDFD"))
        telephone_label.override_background_color(Gtk.StateFlags.NORMAL, rgba)

            # Ajout des clients dans le tableau
        for i, client in enumerate(clients):
                prenom_label = Gtk.Label(client.prenom)
                prenom_label.set_markup("<span size='20000' foreground='#092584'>{}</span>".format(prenom_label.get_text()))  
                tableau.attach(prenom_label, 0, i+1, 1, 1)

                nom_label = Gtk.Label(client.nom)
                nom_label.set_markup("<span size='20000' foreground='#092584'>{}</span>".format(nom_label.get_text()))  
                tableau.attach(nom_label, 1, i+1, 1, 1)

                id_label = Gtk.Label(client.id)
                id_label.set_markup("<span size='20000' foreground='#092584'>{}</span>".format(id_label.get_text()))  
                tableau.attach(id_label, 2, i+1, 1, 1)
                
                telephone_label = Gtk.Label(client.telephone)
                telephone_label.set_markup("<span size='20000' foreground='#092584'>{}</span>".format(telephone_label.get_text()))  
                tableau.attach(telephone_label, 3, i+1, 1, 1)

                 # Bouton de retour
         
        actionbar = Gtk.ActionBar()
        actionbar.set_hexpand(True)
        tableau.attach(actionbar, 1, 5, 2, 1)

        button1 = Gtk.Button("Retour")
        actionbar.pack_start(button1)
        actionbar.pack_end(button1)
        button1.connect("clicked", self.retourner)
    
     def retourner(self, widget):
        self.hide()
        login_window = PageAccueil()
        login_window.show_all() 
pass

if __name__ == "__main__":
    registration_window = PagePrincipale()
    registration_window.connect("destroy", Gtk.main_quit)
    registration_window.show_all()
    Gtk.main()