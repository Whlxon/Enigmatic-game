import pygame as pg

buche = 0

take = ['rock not take', 'rock2 not take']
take_k = ['key not take', 'key2 not take']

rock = pg.image.load('environement/interact/rock.png')
rock2 = pg.image.load('environement/interact/rock.png')

button1_p = pg.image.load('environement/interact/button_up.png')
button1_d = pg.image.load('environement/interact/button_down.png')

button2_p = pg.image.load('environement/interact/button_up.png')
button2_d = pg.image.load('environement/interact/button_down.png')

borne_d = pg.image.load("environement/interact/borne d'indice.png")

key = pg.image.load('environement/interact/key.png')

key2 = pg.image.load('environement/interact/key.png')

porte = pg.image.load('environement/interact/porte fermer.png')

porte_hitbox = pg.image.load('environement/interact/porte hitbox.png')

porte2 = pg.image.load('environement/interact/porte2.png')

jean_pierre = pg.image.load('environement/interact/pnj.png')

baque1_remplit = pg.image.load('environement/interact/baque tomate.png')
baque2_remplit = pg.image.load('environement/interact/baque tomate.png')

drop_zone = pg.image.load('environement/interact/drop_zone.png')

broken_bridge = pg.image.load('environement/interact/bridge broken.png')

bridge = pg.image.load('environement/interact/bridge.png')

jeton_int = pg.image.load('environement/interact/jeton_interact.png')

train = pg.image.load('environement/interact/train.png')

destroyed_train = pg.image.load('environement/interact/destroyed_train.png')

stick = pg.image.load('environement/interact/stick.png')

étincelle1 = pg.image.load('environement/interact/étincelle1.png')

étincelle2 = pg.image.load('environement/interact/étincelle2.png')

étincelle3 = pg.image.load('environement/interact/étincelle3.png')

étincelle4 = pg.image.load('environement/interact/étincelle4.png')

étincelle5 = pg.image.load('environement/interact/étincelle5.png')

étincelle6 = pg.image.load('environement/interact/étincelle6.png')

nuclear_bomb = pg.image.load('environement/interact/nuclear_bomb.png')

hide_way = pg.image.load('environement/interact/hide_way.png')

good_way = pg.image.load('environement/interact/good_way.png')

hitbox_way = pg.image.load('environement/interact/hitbox_way.png')

hitbox_way_rect = hitbox_way.get_rect()
hitbox_way_mask = pg.mask.from_surface(hitbox_way)

nuc_x, nuc_y = 500, -82

stick_rect = stick.get_rect()
stick_rect.x, stick_rect.y = 500, 585

destroyed_train_rect = train.get_rect()
destroyed_train_rect.x, destroyed_train_rect.y = 1026, 565

train_rect = train.get_rect()
train_rect.x, train_rect.y = 1026, 545

jeton_int_rect = jeton_int.get_rect()

bridge_rect = bridge.get_rect()
bridge_rect.x, bridge_rect.y = 490, 197

broken_bridge_rect = broken_bridge.get_rect()
broken_bridge_rect.x, broken_bridge_rect.y = 490, 197
broken_bridge_mask = pg.mask.from_surface(broken_bridge)
mask_broken_bridge = broken_bridge_mask.to_surface()

drop_zone_rect = drop_zone.get_rect()
drop_zone_rect.x, drop_zone_rect.y = 184, 513

baque2_remplit_rect = baque2_remplit.get_rect()
baque2_remplit_rect.x, baque2_remplit_rect.y = 750, 550
baque2_mask = pg.mask.from_surface(baque2_remplit)
mask_baque2 = baque2_mask.to_surface()

baque1_remplit_rect = baque1_remplit.get_rect()
baque1_remplit_rect.x, baque1_remplit_rect.y = 750, 630
baque1_mask = pg.mask.from_surface(baque1_remplit)
mask_baque1 = baque1_mask.to_surface()

jean_pierre_rect = jean_pierre.get_rect()
jean_pierre_rect.x, jean_pierre_rect.y = 85, 425

porteh_rect = porte_hitbox.get_rect()
porteh_rect.x, porteh_rect.y = 414, 200

porte_rect = porte.get_rect()
porte_rect.x, porte_rect.y = 414, 200
porte_mask = pg.mask.from_surface(porte)

key2_rect = key2.get_rect()
key2_rect.x, key2_rect.y = 0, 0

key_rect = key.get_rect()
key_rect.x, key_rect.y = 230, 285

borne_d_rect = borne_d.get_rect()
borne_d_rect.x, borne_d_rect.y = 700, 770
borne_d_mask = pg.mask.from_surface(borne_d)

button1_rect = button1_d.get_rect()
button1_rect.x, button1_rect.y = 230, 120

button2_rect = button2_d.get_rect()
button2_rect.x, button2_rect.y = 615, 485

rock1_rect = rock.get_rect()
rock1_rect.x, rock1_rect.y = 432, 365

rock2_rect = rock2.get_rect()
rock2_rect.x, rock2_rect.y = 550, 735

#pour s'en sortir on importe a part les different piece du puzzle
piece1 = pg.image.load('environement/interact/piece_puzzle/piece1.png')
piece1_rect = piece1.get_rect()
piece1_rect.x, piece1_rect.y = 90, 80

piece2 = pg.image.load('environement/interact/piece_puzzle/piece2.png')
piece2_rect = piece2.get_rect()
piece2_rect.x, piece2_rect.y = 825, 142

piece3 = pg.image.load('environement/interact/piece_puzzle/piece3.png')
piece3_rect = piece3.get_rect()
piece3_rect.x, piece3_rect.y = 540, 142

piece4 = pg.image.load('environement/interact/piece_puzzle/piece4.png')
piece4_rect = piece4.get_rect()
piece4_rect.x, piece4_rect.y = 500, 512

piece5 = pg.image.load('environement/interact/piece_puzzle/piece5.png')
piece5_rect = piece5.get_rect()
piece5_rect.x, piece5_rect.y = 825, 204

piece6 = pg.image.load('environement/interact/piece_puzzle/piece6.png')
piece6_rect = piece6.get_rect()
piece6_rect.x, piece6_rect.y = 490, 142

piece7 = pg.image.load('environement/interact/piece_puzzle/piece7.png')
piece7_rect = piece7.get_rect()
piece7_rect.x, piece7_rect.y = 590, 142

piece8 = pg.image.load('environement/interact/piece_puzzle/piece8.png')
piece8_rect = piece8.get_rect()
piece8_rect.x, piece8_rect.y = 875, 204

piece9 = pg.image.load('environement/interact/piece_puzzle/piece9.png')
piece9_rect = piece9.get_rect()
piece9_rect.x, piece9_rect.y = 875, 328

piece10 = pg.image.load('environement/interact/piece_puzzle/piece10.png')
piece10_rect = piece10.get_rect()
piece10_rect.x, piece10_rect.y = 390, 80

piece11 = pg.image.load('environement/interact/piece_puzzle/piece11.png')
piece11_rect = piece11.get_rect()
piece11_rect.x, piece11_rect.y = 825, 266

piece12 = pg.image.load('environement/interact/piece_puzzle/piece12.png')
piece12_rect = piece12.get_rect()
piece12_rect.x, piece12_rect.y = 875, 266

piece13 = pg.image.load('environement/interact/piece_puzzle/piece13.png')
piece13_rect = piece13.get_rect()
piece13_rect.x, piece13_rect.y = 440, 80

piece14 = pg.image.load('environement/interact/piece_puzzle/piece14.png')
piece14_rect = piece14.get_rect()
piece14_rect.x, piece14_rect.y = 440, 142

piece15 = pg.image.load('environement/interact/piece_puzzle/piece15.png')
piece15_rect = piece15.get_rect()
piece15_rect.x, piece15_rect.y = 500, 450

piece16 = pg.image.load('environement/interact/piece_puzzle/piece16.png')
piece16_rect = piece16.get_rect()
piece16_rect.x, piece16_rect.y = 505, 35

piece17 = pg.image.load('environement/interact/piece_puzzle/piece17.png')
piece17_rect = piece17.get_rect()
piece17_rect.x, piece17_rect.y = 90, 266

piece18 = pg.image.load('environement/interact/piece_puzzle/piece18.png')
piece18_rect = piece18.get_rect()
piece18_rect.x, piece18_rect.y = 490, 80

piece19 = pg.image.load('environement/interact/piece_puzzle/piece19.png')
piece19_rect = piece19.get_rect()
piece19_rect.x, piece19_rect.y = 825, 328

piece20 = pg.image.load('environement/interact/piece_puzzle/piece20.png')
piece20_rect = piece20.get_rect()
piece20_rect.x, piece20_rect.y = 290, 80

piece21 = pg.image.load('environement/interact/piece_puzzle/piece21.png')
piece21_rect = piece21.get_rect()
piece21_rect.x, piece21_rect.y = 390, 142

piece22 = pg.image.load('environement/interact/piece_puzzle/piece22.png')
piece22_rect = piece22.get_rect()
piece22_rect.x, piece22_rect.y = 875, 80

piece23 = pg.image.load('environement/interact/piece_puzzle/piece23.png')
piece23_rect = piece23.get_rect()
piece23_rect.x, piece23_rect.y = 500, 650

piece24 = pg.image.load('environement/interact/piece_puzzle/piece24.png')
piece24_rect = piece24.get_rect()
piece24_rect.x, piece24_rect.y = 590, 80

piece25 = pg.image.load('environement/interact/piece_puzzle/piece25.png')
piece25_rect = piece25.get_rect()
piece25_rect.x, piece25_rect.y = 500, 712

piece26 = pg.image.load('environement/interact/piece_puzzle/piece26.png')
piece26_rect = piece26.get_rect()
piece26_rect.x, piece26_rect.y = 540, 80

piece27 = pg.image.load('environement/interact/piece_puzzle/piece27.png')
piece27_rect = piece27.get_rect()
piece27_rect.x, piece27_rect.y = 875, 142

piece28 = pg.image.load('environement/interact/piece_puzzle/piece28.png')
piece28_rect = piece28.get_rect()
piece28_rect.x, piece28_rect.y = 140, 142

piece29 = pg.image.load('environement/interact/piece_puzzle/piece29.png')
piece29_rect = piece29.get_rect()
piece29_rect.x, piece29_rect.y = 725, 328

piece30 = pg.image.load('environement/interact/piece_puzzle/piece30.png')
piece30_rect = piece30.get_rect()
piece30_rect.x, piece30_rect.y = 90, 204

piece31 = pg.image.load('environement/interact/piece_puzzle/piece31.png')
piece31_rect = piece31.get_rect()
piece31_rect.x, piece31_rect.y = 775, 80

piece32 = pg.image.load('environement/interact/piece_puzzle/piece32.png')
piece32_rect = piece32.get_rect()
piece32_rect.x, piece32_rect.y = 140, 80

piece33 = pg.image.load('environement/interact/piece_puzzle/piece33.png')
piece33_rect = piece33.get_rect()
piece33_rect.x, piece33_rect.y = 240, 80

piece34 = pg.image.load('environement/interact/piece_puzzle/piece34.png')
piece34_rect = piece34.get_rect()
piece34_rect.x, piece34_rect.y = 725, 266

piece35 = pg.image.load('environement/interact/piece_puzzle/piece35.png')
piece35_rect = piece35.get_rect()
piece35_rect.x, piece35_rect.y = 90, 142

piece36 = pg.image.load('environement/interact/piece_puzzle/piece36.png')
piece36_rect = piece36.get_rect()
piece36_rect.x, piece36_rect.y = 340, 80

piece37 = pg.image.load('environement/interact/piece_puzzle/piece37.png')
piece37_rect = piece37.get_rect()
piece37_rect.x, piece37_rect.y = 290, 142

piece38 = pg.image.load('environement/interact/piece_puzzle/piece38.png')
piece38_rect = piece38.get_rect()
piece38_rect.x, piece38_rect.y = 190, 142

piece39 = pg.image.load('environement/interact/piece_puzzle/piece39.png')
piece39_rect = piece39.get_rect()
piece39_rect.x, piece39_rect.y = 340, 328

piece40 = pg.image.load('environement/interact/piece_puzzle/piece40.png')
piece40_rect = piece40.get_rect()
piece40_rect.x, piece40_rect.y = 240, 328

piece41 = pg.image.load('environement/interact/piece_puzzle/piece41.png')
piece41_rect = piece41.get_rect()
piece41_rect.x, piece41_rect.y = 675, 80

piece42 = pg.image.load('environement/interact/piece_puzzle/piece42.png')
piece42_rect = piece42.get_rect()
piece42_rect.x, piece42_rect.y = 725, 204

piece43 = pg.image.load('environement/interact/piece_puzzle/piece43.png')
piece43_rect = piece43.get_rect()
piece43_rect.x, piece43_rect.y = 340, 142

piece44 = pg.image.load('environement/interact/piece_puzzle/piece44.png')
piece44_rect = piece44.get_rect()
piece44_rect.x, piece44_rect.y = 775, 142

piece45 = pg.image.load('environement/interact/piece_puzzle/piece45.png')
piece45_rect = piece45.get_rect()
piece45_rect.x, piece45_rect.y = 190, 80

piece46 = pg.image.load('environement/interact/piece_puzzle/piece46.png')
piece46_rect = piece46.get_rect()
piece46_rect.x, piece46_rect.y = 190, 266

piece47 = pg.image.load('environement/interact/piece_puzzle/piece47.png')
piece47_rect = piece47.get_rect()
piece47_rect.x, piece47_rect.y = 140, 266

piece48 = pg.image.load('environement/interact/piece_puzzle/piece48.png')
piece48_rect = piece48.get_rect()
piece48_rect.x, piece48_rect.y = 675, 142

piece49 = pg.image.load('environement/interact/piece_puzzle/piece49.png')
piece49_rect = piece49.get_rect()
piece49_rect.x, piece49_rect.y = 240, 142

piece50 = pg.image.load('environement/interact/piece_puzzle/piece50.png')
piece50_rect = piece50.get_rect()
piece50_rect.x, piece50_rect.y = 290, 204

piece51 = pg.image.load('environement/interact/piece_puzzle/piece51.png')
piece51_rect = piece51.get_rect()
piece51_rect.x, piece51_rect.y = 90, 328

piece52 = pg.image.load('environement/interact/piece_puzzle/piece52.png')
piece52_rect = piece52.get_rect()
piece52_rect.x, piece52_rect.y = 725, 142

piece53 = pg.image.load('environement/interact/piece_puzzle/piece53.png')
piece53_rect = piece53.get_rect()
piece53_rect.x, piece53_rect.y = 775, 266 

piece54 = pg.image.load('environement/interact/piece_puzzle/piece54.png')
piece54_rect = piece54.get_rect()
piece54_rect.x, piece54_rect.y = 775, 204

piece55 = pg.image.load('environement/interact/piece_puzzle/piece55.png')
piece55_rect = piece55.get_rect()
piece55_rect.x, piece55_rect.y = 190, 204

piece56 = pg.image.load('environement/interact/piece_puzzle/piece56.png')
piece56_rect = piece56.get_rect()
piece56_rect.x, piece56_rect.y = 675, 204

piece57 = pg.image.load('environement/interact/piece_puzzle/piece57.png')
piece57_rect = piece57.get_rect()
piece57_rect.x, piece57_rect.y = 140, 204

piece58 = pg.image.load('environement/interact/piece_puzzle/piece58.png')
piece58_rect = piece58.get_rect()
piece58_rect.x, piece58_rect.y = 340, 266

piece59 = pg.image.load('environement/interact/piece_puzzle/piece59.png')
piece59_rect = piece59.get_rect()
piece59_rect.x, piece59_rect.y = 725, 80

piece60 = pg.image.load('environement/interact/piece_puzzle/piece60.png')
piece60_rect = piece60.get_rect()
piece60_rect.x, piece60_rect.y = 340, 204

piece61 = pg.image.load('environement/interact/piece_puzzle/piece61.png')
piece61_rect = piece61.get_rect()
piece61_rect.x, piece61_rect.y = 190, 328

piece62 = pg.image.load('environement/interact/piece_puzzle/piece62.png')
piece62_rect = piece62.get_rect()
piece62_rect.x, piece62_rect.y = 825, 80

piece63 = pg.image.load('environement/interact/piece_puzzle/piece63.png')
piece63_rect = piece63.get_rect()
piece63_rect.x, piece63_rect.y = 290, 266

piece64 = pg.image.load('environement/interact/piece_puzzle/piece64.png')
piece64_rect = piece64.get_rect()
piece64_rect.x, piece64_rect.y = 675, 328

piece65 = pg.image.load('environement/interact/piece_puzzle/piece65.png')
piece65_rect = piece65.get_rect()
piece65_rect.x, piece65_rect.y = 240, 204

piece66 = pg.image.load('environement/interact/piece_puzzle/piece66.png')
piece66_rect = piece66.get_rect()
piece66_rect.x, piece66_rect.y = 775, 328

piece67 = pg.image.load('environement/interact/piece_puzzle/piece67.png')
piece67_rect = piece67.get_rect()
piece67_rect.x, piece67_rect.y = 675, 266

piece68 = pg.image.load('environement/interact/piece_puzzle/piece68.png')
piece68_rect = piece68.get_rect()
piece68_rect.x, piece68_rect.y = 240, 266

piece69 = pg.image.load('environement/interact/piece_puzzle/piece69.png')
piece69_rect = piece69.get_rect()
piece69_rect.x, piece69_rect.y = 290, 328

piece70 = pg.image.load('environement/interact/piece_puzzle/piece70.png')
piece70_rect = piece70.get_rect()
piece70_rect.x, piece70_rect.y = 140, 328





#on importe les case attribuer au pieces de puzzle

cases1 = pg.image.load('environement\interact\piece_zone.png')
cases1_rect = cases1.get_rect()
cases1_rect.x, cases1_rect.y = 375, 175

cases2 = pg.image.load('environement\interact\piece_zone.png')
cases2_rect = cases2.get_rect()
cases2_rect.x, cases2_rect.y = 400, 175

cases3 = pg.image.load('environement\interact\piece_zone.png')
cases3_rect = cases3.get_rect()
cases3_rect.x, cases3_rect.y = 425, 175

cases4 = pg.image.load('environement\interact\piece_zone.png')
cases4_rect = cases4.get_rect()
cases4_rect.x, cases4_rect.y = 450, 175

cases5 = pg.image.load('environement\interact\piece_zone.png')
cases5_rect = cases5.get_rect()
cases5_rect.x, cases5_rect.y = 475, 175

cases6 = pg.image.load('environement\interact\piece_zone.png')
cases6_rect = cases6.get_rect()
cases6_rect.x, cases6_rect.y = 500, 175

cases7 = pg.image.load('environement\interact\piece_zone.png')
cases7_rect = cases7.get_rect()
cases7_rect.x, cases7_rect.y = 525, 175

cases8 = pg.image.load('environement\interact\piece_zone.png')
cases8_rect = cases8.get_rect()
cases8_rect.x, cases8_rect.y = 550, 175

cases9 = pg.image.load('environement\interact\piece_zone.png')
cases9_rect = cases9.get_rect()
cases9_rect.x, cases9_rect.y = 575, 175

cases10 = pg.image.load('environement\interact\piece_zone.png')
cases10_rect = cases10.get_rect()
cases10_rect.x, cases10_rect.y = 600, 175

cases11 = pg.image.load('environement\interact\piece_zone.png')
cases11_rect = cases11.get_rect()
cases11_rect.x, cases11_rect.y = 375, 200

cases12 = pg.image.load('environement\interact\piece_zone.png')
cases12_rect = cases12.get_rect()
cases12_rect.x, cases12_rect.y = 400, 200

cases13 = pg.image.load('environement\interact\piece_zone.png')
cases13_rect = cases13.get_rect()
cases13_rect.x, cases13_rect.y = 425, 200

cases14 = pg.image.load('environement\interact\piece_zone.png')
cases14_rect = cases14.get_rect()
cases14_rect.x, cases14_rect.y = 450, 200

cases15 = pg.image.load('environement\interact\piece_zone.png')
cases15_rect = cases15.get_rect()
cases15_rect.x, cases15_rect.y = 475, 200

cases16 = pg.image.load('environement\interact\piece_zone.png')
cases16_rect = cases16.get_rect()
cases16_rect.x, cases16_rect.y = 500, 200

cases17 = pg.image.load('environement\interact\piece_zone.png')
cases17_rect = cases17.get_rect()
cases17_rect.x, cases17_rect.y = 525, 200

cases18 = pg.image.load('environement\interact\piece_zone.png')
cases18_rect = cases18.get_rect()
cases18_rect.x, cases18_rect.y = 550, 200

cases19 = pg.image.load('environement\interact\piece_zone.png')
cases19_rect = cases19.get_rect()
cases19_rect.x, cases19_rect.y = 575, 200

cases20 = pg.image.load('environement\interact\piece_zone.png')
cases20_rect = cases20.get_rect()
cases20_rect.x, cases20_rect.y = 600, 200

cases21 = pg.image.load('environement\interact\piece_zone.png')
cases21_rect = cases21.get_rect()
cases21_rect.x, cases21_rect.y = 375, 225

cases22 = pg.image.load('environement\interact\piece_zone.png')
cases22_rect = cases22.get_rect()
cases22_rect.x, cases22_rect.y = 400, 225

cases23 = pg.image.load('environement\interact\piece_zone.png')
cases23_rect = cases23.get_rect()
cases23_rect.x, cases23_rect.y = 425, 225

cases24 = pg.image.load('environement\interact\piece_zone.png')
cases24_rect = cases24.get_rect()
cases24_rect.x, cases24_rect.y = 450, 225

cases25 = pg.image.load('environement\interact\piece_zone.png')
cases25_rect = cases25.get_rect()
cases25_rect.x, cases25_rect.y = 475, 225

cases26 = pg.image.load('environement\interact\piece_zone.png')
cases26_rect = cases26.get_rect()
cases26_rect.x, cases26_rect.y = 500, 225

cases27 = pg.image.load('environement\interact\piece_zone.png')
cases27_rect = cases27.get_rect()
cases27_rect.x, cases27_rect.y = 525, 225

cases28 = pg.image.load('environement\interact\piece_zone.png')
cases28_rect = cases28.get_rect()
cases28_rect.x, cases28_rect.y = 550, 225

cases29 = pg.image.load('environement\interact\piece_zone.png')
cases29_rect = cases29.get_rect()
cases29_rect.x, cases29_rect.y = 575, 225

cases30 = pg.image.load('environement\interact\piece_zone.png')
cases30_rect = cases30.get_rect()
cases30_rect.x, cases30_rect.y = 600, 225

cases31 = pg.image.load('environement\interact\piece_zone.png')
cases31_rect = cases31.get_rect()
cases31_rect.x, cases31_rect.y = 375, 250

cases32 = pg.image.load('environement\interact\piece_zone.png')
cases32_rect = cases32.get_rect()
cases32_rect.x, cases32_rect.y = 400, 250

cases33 = pg.image.load('environement\interact\piece_zone.png')
cases33_rect = cases33.get_rect()
cases33_rect.x, cases33_rect.y = 425, 250

cases34 = pg.image.load('environement\interact\piece_zone.png')
cases34_rect = cases34.get_rect()
cases34_rect.x, cases34_rect.y = 450, 250

cases35 = pg.image.load('environement\interact\piece_zone.png')
cases35_rect = cases35.get_rect()
cases35_rect.x, cases35_rect.y = 475, 250

cases36 = pg.image.load('environement\interact\piece_zone.png')
cases36_rect = cases36.get_rect()
cases36_rect.x, cases36_rect.y = 500, 250

cases37 = pg.image.load('environement\interact\piece_zone.png')
cases37_rect = cases37.get_rect()
cases37_rect.x, cases37_rect.y = 525, 250

cases38 = pg.image.load('environement\interact\piece_zone.png')
cases38_rect = cases38.get_rect()
cases38_rect.x, cases38_rect.y = 550, 250

cases39 = pg.image.load('environement\interact\piece_zone.png')
cases39_rect = cases39.get_rect()
cases39_rect.x, cases39_rect.y = 575, 250

cases40 = pg.image.load('environement\interact\piece_zone.png')
cases40_rect = cases40.get_rect()
cases40_rect.x, cases40_rect.y = 600, 250

cases41 = pg.image.load('environement\interact\piece_zone.png')
cases41_rect = cases41.get_rect()
cases41_rect.x, cases41_rect.y = 375, 275

cases42 = pg.image.load('environement\interact\piece_zone.png')
cases42_rect = cases42.get_rect()
cases42_rect.x, cases42_rect.y = 400, 275

cases43 = pg.image.load('environement\interact\piece_zone.png')
cases43_rect = cases43.get_rect()
cases43_rect.x, cases43_rect.y = 425, 275

cases44 = pg.image.load('environement\interact\piece_zone.png')
cases44_rect = cases44.get_rect()
cases44_rect.x, cases44_rect.y = 450, 275

cases45 = pg.image.load('environement\interact\piece_zone.png')
cases45_rect = cases45.get_rect()
cases45_rect.x, cases45_rect.y = 475, 275

cases46 = pg.image.load('environement\interact\piece_zone.png')
cases46_rect = cases46.get_rect()
cases46_rect.x, cases46_rect.y = 500, 275

cases47 = pg.image.load('environement\interact\piece_zone.png')
cases47_rect = cases47.get_rect()
cases47_rect.x, cases47_rect.y = 525, 275

cases48 = pg.image.load('environement\interact\piece_zone.png')
cases48_rect = cases48.get_rect()
cases48_rect.x, cases48_rect.y = 550, 275

cases49 = pg.image.load('environement\interact\piece_zone.png')
cases49_rect = cases49.get_rect()
cases49_rect.x, cases49_rect.y = 575, 275

cases50 = pg.image.load('environement\interact\piece_zone.png')
cases50_rect = cases50.get_rect()
cases50_rect.x, cases50_rect.y = 600, 275

cases51 = pg.image.load('environement\interact\piece_zone.png')
cases51_rect = cases51.get_rect()
cases51_rect.x, cases51_rect.y = 375, 300

cases52 = pg.image.load('environement\interact\piece_zone.png')
cases52_rect = cases52.get_rect()
cases52_rect.x, cases52_rect.y = 400, 300

cases53 = pg.image.load('environement\interact\piece_zone.png')
cases53_rect = cases53.get_rect()
cases53_rect.x, cases53_rect.y = 425, 300

cases54 = pg.image.load('environement\interact\piece_zone.png')
cases54_rect = cases54.get_rect()
cases54_rect.x, cases54_rect.y = 450, 300

cases55 = pg.image.load('environement\interact\piece_zone.png')
cases55_rect = cases55.get_rect()
cases55_rect.x, cases55_rect.y = 475, 300

cases56 = pg.image.load('environement\interact\piece_zone.png')
cases56_rect = cases56.get_rect()
cases56_rect.x, cases56_rect.y = 500, 300

cases57 = pg.image.load('environement\interact\piece_zone.png')
cases57_rect = cases57.get_rect()
cases57_rect.x, cases57_rect.y = 525, 300

cases58 = pg.image.load('environement\interact\piece_zone.png')
cases58_rect = cases58.get_rect()
cases58_rect.x, cases58_rect.y = 550, 300

cases59 = pg.image.load('environement\interact\piece_zone.png')
cases59_rect = cases59.get_rect()
cases59_rect.x, cases59_rect.y = 575, 300

cases60 = pg.image.load('environement\interact\piece_zone.png')
cases60_rect = cases60.get_rect()
cases60_rect.x, cases60_rect.y = 600, 300

cases61 = pg.image.load('environement\interact\piece_zone.png')
cases61_rect = cases61.get_rect()
cases61_rect.x, cases61_rect.y = 375, 325

cases62 = pg.image.load('environement\interact\piece_zone.png')
cases62_rect = cases62.get_rect()
cases62_rect.x, cases62_rect.y = 400, 325

cases63 = pg.image.load('environement\interact\piece_zone.png')
cases63_rect = cases63.get_rect()
cases63_rect.x, cases63_rect.y = 425, 325

cases64 = pg.image.load('environement\interact\piece_zone.png')
cases64_rect = cases64.get_rect()
cases64_rect.x, cases64_rect.y = 450, 325

cases65 = pg.image.load('environement\interact\piece_zone.png')
cases65_rect = cases65.get_rect()
cases65_rect.x, cases65_rect.y = 475, 325

cases66 = pg.image.load('environement\interact\piece_zone.png')
cases66_rect = cases66.get_rect()
cases66_rect.x, cases66_rect.y = 500, 325

cases67 = pg.image.load('environement\interact\piece_zone.png')
cases67_rect = cases67.get_rect()
cases67_rect.x, cases67_rect.y = 525, 325

cases68 = pg.image.load('environement\interact\piece_zone.png')
cases68_rect = cases68.get_rect()
cases68_rect.x, cases68_rect.y = 550, 325

cases69 = pg.image.load('environement\interact\piece_zone.png')
cases69_rect = cases69.get_rect()
cases69_rect.x, cases69_rect.y = 575, 325

cases70 = pg.image.load('environement\interact\piece_zone.png')
cases70_rect = cases70.get_rect()
cases70_rect.x, cases70_rect.y = 600, 325

