history_test_file = '''
#Uppland, contains Stockholm, Uppsala & Nyköping.

add_core = SWE
owner = SWE
controller = SWE
culture = swedish
religion = catholic
hre = no
base_tax = 5 
base_production = 5
trade_goods = grain
base_manpower = 3
capital = "Stockholm"
is_city = yes
discovered_by = eastern
discovered_by = western
discovered_by = muslim
discovered_by = ottoman
extra_cost = 16
center_of_trade = 2


1436.4.28 = { revolt = { type = pretender_rebels size = 1 leader = "Karl Knutsson Bonde" } controller = REB } # Karl Knutsson Bonde marsh on Stockholm
1438.3.6 = { revolt = {} controller = SWE } # Unclear date
1438.10.1 = { revolt = { type = pretender_rebels size = 1 leader = "Karl Knutsson Bonde" } controller = REB } # Unclear date
1440.9.1 = { revolt = {} controller = SWE } # Christopher III elected Union King
1448.6.20 = { revolt = {} controller = SWE } # Karl VIII is elected king of Sweden
1501.8.1 = { controller = DAN } # Danish loyalists at Swedish DoW and breaking of vassalage
1502.5.9 = { controller = SWE } # Retaken by Sweden
1523.6.7 = { base_manpower = 4 } # Kgl.Drabantkåren/Svea Livgarde
1527.6.1 = {
	religion = protestant
	reformation_center = protestant
}
1598.8.12 = { controller = PLC } # Sigismund tries to reconquer his crown
1598.12.15 = { controller = SWE } # Duke Karl get it back
1617.1.1 = { 
	base_tax = 6 
	base_production = 6 
} # Stockholm become Baltic Metropol
'''
cultures_test_file = '''
je_tupi = { # Tupi
	graphical_culture = northamericagfx
	
	tupinamba = {
		primary = TPQ
		dynasty_names = {
			Piratininga Tabajara Temiminó Tamoio Tabajara Caeté Tupinaé Temiminó Tupina Aricobé
		}
		male_names = {
			Tibiriçá Piquerobi Caiubi Ramalho Italo Arah Pirijá Arata Toruí Mbicy
		}
		female_names = {
			Bartira Potira Porasy Jougousa Azelene
		}
	}
	guarani = {
		primary = GUA
		dynasty_names = {
			Mbigua Caracara Timbu Tucague Calchagui Quiloazaz Cario Itatine Tarci Bomboi Curupaiti Curumai Caaigua Tape Ciriguana
		}
		male_names = {
			Angatupyry Apytere Arandu Araresa Amaru Amapytu Amangy Aravera Arasunu Aratiri Chavuku Jakaira Karai 
			Katupyry Kuarahy Kuarahyrese Maitei Mba'ehory Mbarakapu Namandu Tajy Tatarendy Tatajyva Tatapytu 
			Tuvicha Ygary Tekokatu
		}
		female_names = {
			Bartira Potira Porasy Jougousa Azelene
		}
	}
}

je = {
	graphical_culture = northamericagfx
	charruan = {
		primary = CUA
		dynasty_names = {
			Sénaqué Sira Gununusa Puyucahua Mataojo Igualdad Yaró Guenoa Bohané Minuan
		}
		male_names = {
			Zapicán Abayubá Vaimaca Perú Senacua Tabaré Itanú Yrupé Jasymimbí Tacuabé Vaimaca-Pirú
		}
		female_names = {
			Bartira Potira Porasy Jougousa Azelene
		}
	}
	ge = {
		primary = TUA
		dynasty_names = {
			Aimoré Prajé Takrukrak Krekmún Ituêto Futikrak Gueren Gutucrac Mekmek Minhagiran Nakrehê Naknyanúk
		}
		male_names = {
			Jandui Raoni Janduwy Caracara Karupoto
		}
		female_names = {
			Bartira Potira Porasy Jougousa Azelene
		}
	}
}
'''
country_test_file = '''
#Country Name: Please see filename.

graphical_culture = inuitgfx

color = { 201 197 124 }

revolutionary_colors = { 12 16 0 }

historical_idea_groups = {
	religious_ideas
	defensive_ideas
	offensive_ideas
	trade_ideas
	diplomatic_ideas
	plutocracy_ideas
	spy_ideas
	economic_ideas
}

historical_units = {
	japanese_archer
	eastern_bow
	japanese_footsoldier
	japanese_samurai
	asian_arquebusier
	asian_charge_cavalry
	asian_mass_infantry
	asian_musketeer
	reformed_asian_musketeer
	reformed_asian_cavalry
}

monarch_names = {	
	"Koshamain #0" = 15
	"Shakushain #0" = 15
	"Kamokutain #0" = 15
	"Onibishi #0" = 15
	"Penri #0" = 15
	"Piripos #0" = 15
	"Takatsuki #0" = 15
	
	"Monashir #0" = -1
	"Etunrachich #0" = -1
	"Toitoi #0" = -1
}

leader_names = {
	Shibushari Hae Betsu Shiraoi Kurasi Kakizaki Ponyanpe Shirokani Otona Ekashi Saru Usu
}

ship_names = {
	Monashir Etunrachich Toitoi Shiratekka Menkakush Horpecha Huisak Opere Unkatuye Umoshmatek
}
'''