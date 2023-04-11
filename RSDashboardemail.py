import win32com.client as win32
import datetime
from datetime import date


def rs_compliace_send_outlook_email():
    # construct Outlook application instance
    olApp = win32.Dispatch('Outlook.Application')
    olNS = olApp.GetNameSpace('MAPI')

    # construct the email item object
    mailItem = olApp.CreateItem(0)
    mailItem.Subject = 'RS Dashboard and RS Compliance Report {0}'.format(
        datetime.date.today())
    mailItem.BodyFormat = 1
    mailItem.Body = """
    Hi All,  \n
    The Related Services Dashboard and RS Compliance Report are updated and posted to SharePoint. \n
    Thank you!  
    """.format(date.today().strftime("%Y%m%d"))
    mailItem.To = 'Vidhi Dharia <vdharia@schools.nyc.gov>; Volpe Cen <CVolpe4@schools.nyc.gov>; Smith Samantha <SSmith110@schools.nyc.gov>; Dedaj Victoria <VDedaj@schools.nyc.gov>; Burnside Eric <EBurnside@schools.nyc.gov>; Odonnell Tricia (09X294) <TOdonnell2@schools.nyc.gov>; Mcfadden Melinda <MMcfadden9@schools.nyc.gov>; Rambaran Stephanie <SRambaran2@schools.nyc.gov>; Lipkowitz Michael <MLipkowitz@schools.nyc.gov>; Lewis Abbey <ALewis22@schools.nyc.gov>; Livingston Stacy <SLivingston2@schools.nyc.gov>; Bajana Sarah <SBajana@schools.nyc.gov>;Edwards Erin <EEdwards14@schools.nyc.gov>; Oppenheimer Daniella <doppenheimer3@schools.nyc.gov>; Demosthenes Aisha <ademosthenes@schools.nyc.gov>; Asaro Michelle <MAsaro3@schools.nyc.gov>;Galaise Jeffrey <JGalaise@schools.nyc.gov>; Johal Kamajit <KJohal@schools.nyc.gov>; Rivera Ivelisse <IRivera22@schools.nyc.gov>; Chasabenis Stamatis <SChasab@schools.nyc.gov>; Chan Lucilla <LChan10@schools.nyc.gov>;Lavergne Shakir <SLavergne@schools.nyc.gov>; Singleton Michelle <MSingle@schools.nyc.gov>; Sam Sasha <SSam2@schools.nyc.gov>; Miragliotta Carla <cmiragliotta@schools.nyc.gov>; Goodman Margaret <mgoodman3@schools.nyc.gov>; Smith Samantha <SSmith110@schools.nyc.gov>;Richardson Muriel <MRichardson3@schools.nyc.gov>;Alcantara Fatima <FAlcantara@schools.nyc.gov>; Alexander Carmen <CAlexan2@schools.nyc.gov>; Allen Michele <MAllen5@schools.nyc.gov>; \
    Antrobus Vann Abigail <AAntrobus@schools.nyc.gov>; Anzalone Christopher <CAnzalone2@schools.nyc.gov>; Aridas Cynthia <CAridas@schools.nyc.gov>;  \
    Bascoe Tanika <TBascoe@schools.nyc.gov>; Bastien-reneliq Stacy <SBastien@schools.nyc.gov>; Battista Michael <MBattis@schools.nyc.gov>; Ben-Moshe Yael <YBen-Moshe@schools.nyc.gov>; \
    Bernstein Edward <EBernstein6@schools.nyc.gov>; Berry Raquel <RBerry2@schools.nyc.gov>; Bethea Jenel <JBethea@schools.nyc.gov>; Bishop Andrea <ABishop3@schools.nyc.gov>; \
    Blitman Sara <SBlitman@schools.nyc.gov>; Bochbot Deborah <DBochbo@schools.nyc.gov>; Boone Cynthia <CBoone@schools.nyc.gov>; Brodsky Jacob <JBrodsky@schools.nyc.gov>; \
    Brown Harris Daria <dbrown6@schools.nyc.gov>; Brown Tiffany <TBrown70@schools.nyc.gov>; Brownstein Wendy <WBrownstein@schools.nyc.gov>; Burgos Evelyn <EBurgos2@schools.nyc.gov>; \
    Calliste Lesley Ann <LCallis@schools.nyc.gov>; Campos Yesenia <YCampos3@schools.nyc.gov>; Carrington Desiree <DCARRINGTON5@schools.nyc.gov>; Ceretti Michael <MCerett@schools.nyc.gov>; \
    Chall Brandon <BChall@schools.nyc.gov>; Chu Yuet <YChu@schools.nyc.gov>; Cirillo Catherine <CCirill@schools.nyc.gov>; Connelly Suzanne <SConnelly5@schools.nyc.gov>; \
    Cook Latipha <LCook8@schools.nyc.gov>; Cooper-Champion Tonya <disabled.TCooper2@schools.nyc.gov>; Cotler Debbie <DCotler@schools.nyc.gov>; Coursey Tara <TCoursey@schools.nyc.gov>; \
    Culbert Samantha <SCulbert@schools.nyc.gov>; Cummings Kisha <KCummings5@schools.nyc.gov>; Dandrea Kristyn <KDandrea@schools.nyc.gov>; Danker Jared <JDanker@schools.nyc.gov>; \
    Dapontes Stavroula <SDapontes@schools.nyc.gov>; Darrigo Dawn <DDarrigo@schools.nyc.gov>; Davis Mona <MDavis22@schools.nyc.gov>; De La Rosa Karen <KDeLaRosa@schools.nyc.gov>; \
    Degramont Darlyne <DDegramont@schools.nyc.gov>; Demosthenes Aisha <ADemosthenes@schools.nyc.gov>; Dicaro Jennifer <JDicaro@schools.nyc.gov>; Dickar Maryann <MDickar2@schools.nyc.gov>; \
    Difiore Joy <JDifiore3@schools.nyc.gov>; Dockery Smith Cecilia <CDockerySmith2@schools.nyc.gov>; Dorcelly Michael <MDorcelly@schools.nyc.gov>; Driesman Wendy <WDriesm@schools.nyc.gov>; \
    Edwards Ebony <disabled.EEdwards2@schools.nyc.gov>; Edwards Tabatha <TEdwards14@schools.nyc.gov>; Ehrenberg Debra <DEhrenberg@schools.nyc.gov>; Epstein Susan <SEpstein5@schools.nyc.gov>; \
    Escollies Iris <IEscoll@schools.nyc.gov>; Ewing Eric <EEwing@schools.nyc.gov>; Fabel Suzanne <SFabel@schools.nyc.gov>; Fenice Melissa <MFenice@schools.nyc.gov>; Fenoaltea Gina <GFenoaltea@schools.nyc.gov>; \
    Ferraiola Lisa <LFerrai@schools.nyc.gov>; Ferreira Giselle <GFerreira@schools.nyc.gov>; Figaro Jenny <JFigaro@schools.nyc.gov>; Foti Christina <CFoti@schools.nyc.gov>; Gallano Michael <MGallano2@schools.nyc.gov>; \
    Galvin Elizabeth <EGalvin4@schools.nyc.gov>; Gardner Sean <SGardner@schools.nyc.gov>; Gavryushenko Sergey <SGavryushenko@schools.nyc.gov>; George Monica <MGeorge@schools.nyc.gov>; Gold Seth <SGold6@schools.nyc.gov>; \
    Goldberg Caren <disabled.CGoldberg6@schools.nyc.gov>; Gonzalez Iris <IGonzal3@schools.nyc.gov>; Gonzalez Jorge <disabled.JGonzalez3@schools.nyc.gov>; Greene Shelley <disabled.SGreene8@schools.nyc.gov>; \
    Greenman Lauren <LGreenman2@schools.nyc.gov>; Groll Janice <JGroll@schools.nyc.gov>; Guercio Eileen <EGuercio@schools.nyc.gov>; Hammer John <JHammer4@schools.nyc.gov>; \
    Harris-pearson Tara <THarrispearson@schools.nyc.gov>; Henein Heba <HHenein@schools.nyc.gov>; Hinkley Michelle <MHinkley@schools.nyc.gov>; Hinton Sheila <SHinton2@schools.nyc.gov>; \
    Holbrook Daniel <DHolbrook2@schools.nyc.gov>; Hom David <DHom@schools.nyc.gov>; Hughes Rose Marie <RHughes4@schools.nyc.gov>; Inzerelli Antonietta <AInzerelli@schools.nyc.gov>; \
    Jean Claude Richard <RJeanCl@schools.nyc.gov>; Jean Guyline <JGuyline@schools.nyc.gov>; Jenkins Jacqueline <JJenkins8@schools.nyc.gov>; \
    Jennings Gregory <GJennin@schools.nyc.gov>; Johal Kamajit <KJohal@schools.nyc.gov>; Johnson Daly Veronica <VJohnsonDaly@schools.nyc.gov>; Jones Juliette <JJones42@schools.nyc.gov>; \
    Jones Kivel <KJones46@schools.nyc.gov>; Joshi Manasi <MJoshi5@schools.nyc.gov>; Kagimbi Loise <LKagimbi2@schools.nyc.gov>; Karty Alison <AKarty@schools.nyc.gov>; Katz Chana <CKatz6@schools.nyc.gov>; \
    Kaufman Helen <HKaufma@schools.nyc.gov>; Kessler Rizzo Jessica <JKessler6@schools.nyc.gov>; Khan Ahsan <disabled.AKhan37@schools.nyc.gov>; Kim Andrea <AKim14@schools.nyc.gov>; Kim Virginia <disabled.VKim@schools.nyc.gov>; \
    King Kathleen <KKing@schools.nyc.gov>; Kip Carlotta <disabled.CKip@schools.nyc.gov>; Kish Lauren <LKish@schools.nyc.gov>; Konig Phillip <PKonig@schools.nyc.gov>; Kopiec Robert <RKopiec@schools.nyc.gov>; \
    Korman Alice <AKorman@schools.nyc.gov>; Kostel Matt (750000) <MKostel@schools.nyc.gov>; Krayets Alexandra <AKrayets@schools.nyc.gov>; Kutner Hallie <HKutner@schools.nyc.gov>; Gaynor Charmaine <CGaynor@schools.nyc.gov>; \
    LaBarbera Judith <JLaBarbera2@schools.nyc.gov>; Lantzounis Alexia <ALantzounis@schools.nyc.gov>; Leong Melanie <MLeong@schools.nyc.gov>; Levine Bambi <disabled.BLevine7@schools.nyc.gov>; Levitt Luisa <LLevitt@schools.nyc.gov>; \
    Lieberman Justin <JLieberman5@schools.nyc.gov>; Lin Lisa <CLin2@schools.nyc.gov>; Louissaint Ketler <KLouiss@schools.nyc.gov>; Lubalin Stephanie <SLubalin@schools.nyc.gov>; Mahamed Saudia <SMahamed@schools.nyc.gov>; Mandel Betsy <BMandel6@schools.nyc.gov>;\
    Martin Glenn <GMartin6@schools.nyc.gov>; Marupaka Phani Bhushan <PMarupaka@schools.nyc.gov>; Marzan Kelly <KMarzan@schools.nyc.gov>; Mason Theodore <tmason@schools.nyc.gov>; Mayilrajan Rajamanickam <RMayilrajan@schools.nyc.gov>; \
    Mcgill Stephanie <SMcGill2@schools.nyc.gov>; Mckenzie Royelle <RMckenzie@schools.nyc.gov>; Mcloughlin Lori Ann <LMcloughlin2@schools.nyc.gov>; Mcnulty Contessa <CMcnulty@schools.nyc.gov>; Miller Abby <AMiller14@schools.nyc.gov>; \
    Miller Michele <MMiller26@schools.nyc.gov>; Mills Mona <disabled.MMills2@schools.nyc.gov>; Mintzer Lisa <LMintze@schools.nyc.gov>; Mitchell Nicole <NMitchell4@schools.nyc.gov>; Monaco Emma <EMonaco@schools.nyc.gov>; Morales Marina <MMorales15@schools.nyc.gov>; \
    Mosquera-Valeri Sandra <SMosquera@schools.nyc.gov>; Motola Phyllis <PMotola@schools.nyc.gov>; Mulcahy Kathleen <KMulcahy@schools.nyc.gov>; Mullen Smith Aileen <AMullen4@schools.nyc.gov>; Navarette Luisa <LNavarette@schools.nyc.gov>; \
    Navarrete Cristina <CNavarrete@schools.nyc.gov>; Nicome Natasha <NNicome@schools.nyc.gov>; Nutter Grace <GNutter@schools.nyc.gov>; Ocharsky Adam <AOcharsky@schools.nyc.gov>; Ogir Crystal <COgir@schools.nyc.gov>; Ojeda Lucy <LOjeda@schools.nyc.gov>; \
    Oleary-Toro Kristen (CFN Cluster 6) <KOleary@schools.nyc.gov>; Onwumere Dora <DOnwumere2@schools.nyc.gov>; Ortiz Jackeline <JOrtiz50@schools.nyc.gov>; Patterson Thomas <TPatterson4@schools.nyc.gov>; Pearson Jamie <JPearson5@schools.nyc.gov>; \
    Perez Ferdinand Blanca <BPerez4@schools.nyc.gov>; Perez Jerry <JPerez42@schools.nyc.gov>; Piccininno Lori <LPiccin@schools.nyc.gov>; Plutchok Malka <MPlutch@schools.nyc.gov>; Polomsky Martin <MPolomsky@schools.nyc.gov>; Powers Alan <APowers3@schools.nyc.gov>; \
    Prowell Sean <SProwell@schools.nyc.gov>; Pupello Lois <LPupell@schools.nyc.gov>; Raguse Betsy <BRaguse@schools.nyc.gov>; Ramirez William <WRamirez@schools.nyc.gov>; Ramones Kimberly <KRamones@schools.nyc.gov>; Ramos Marissa <MRamos60@schools.nyc.gov>; \
    Reese Stephen <SReese2@schools.nyc.gov>; Regan Cori <CRegan@schools.nyc.gov>; Restivo Christopher (75R025) <CRestiv@schools.nyc.gov>; Riccobono Joseph <JRiccobono@schools.nyc.gov>; Robinson Denise <DRobins5@schools.nyc.gov>; Robles Michelle <MRobles3@schools.nyc.gov>; \
    Rodriguez Luisa <disabled.LRodriguez133@schools.nyc.gov>; Rosenberg Aron <ARosenb6@schools.nyc.gov>; Rotenberg Sheri <SRotenberg@schools.nyc.gov>; Rozovskaya Liana <LRozovskaya@schools.nyc.gov>; Rubino Charles <CRubino3@schools.nyc.gov>; \
    Rupnarain Bebi <BRupnar@schools.nyc.gov>; Sackris Brent <BSackris@schools.nyc.gov>; Safyan Diana <DSafyan@schools.nyc.gov>; Sanchez Suzanne <SSanchez8@schools.nyc.gov>; Santos Lais <LSantos8@schools.nyc.gov>; Sattar Maryam <MSattar2@schools.nyc.gov>; \
    Savarin Madeline <MSavarin2@schools.nyc.gov>; Schmitt Peter <PSchmitt@schools.nyc.gov>; Schwartz Devin <DSchwartz9@schools.nyc.gov>; Sealy Marita <disabled.MSealy@schools.nyc.gov>; Segev Shelly <SSegev@schools.nyc.gov>; Seidman Steven <SSeidman4@schools.nyc.gov>; \
    Shats Aleksey <AShats@schools.nyc.gov>; Sippy Sujeeta <SSippy@schools.nyc.gov>; Song Mi Jung Judile <MSong2@schools.nyc.gov>; Stamm Charles <CStamm@schools.nyc.gov>; Stanislas Martina <MStanis@schools.nyc.gov>; Stefkovich Donna <DStefkovich@schools.nyc.gov>; \
    Sylvester Karen <KSylvester4@schools.nyc.gov>; Taharally Christophe <CTaharally@schools.nyc.gov>; Tarnarider Nataly <NTarnarider@schools.nyc.gov>; Tenenbaum Batya <BTenenbaum@schools.nyc.gov>; Terzulli Raffaella <RTerzul@schools.nyc.gov>; Testani Kristin <KTestani@schools.nyc.gov>; \
    Thomas Carin <CThomas82@schools.nyc.gov>; Tomeo Jessica <disabled.JTomeo2@schools.nyc.gov>; Tomeo Julia <JTomeo@schools.nyc.gov>; Torres Angela <ATorres21@schools.nyc.gov>; Trivedi Sejal <STrivedi@schools.nyc.gov>; Tsirulnikov Zoya <ZTsirulnikov@schools.nyc.gov>; \
    Tumelty Margaret <MTumelty@schools.nyc.gov>; Valentine Valerie <VValentine@schools.nyc.gov>; Van Biema Michael <MVanBiema@schools.nyc.gov>; Van Holt Lisa <LVanHolt@schools.nyc.gov>; VanZetta Christine <CVanzet@schools.nyc.gov>; Vasquez Daliz <DVasquez3@schools.nyc.gov>; \
    Walker Karin <KWalker@schools.nyc.gov>; Wang Yanjing <YWang36@schools.nyc.gov>; Ware-Malleuve Kismet <KWareMalleuve@schools.nyc.gov>; Weaver Joseph <JWeaver2@schools.nyc.gov>; Wedderburn Simpson Barbara <BWedder@schools.nyc.gov>; Weiss Yael <YWeiss@schools.nyc.gov>;\
    Whitfield Buffie <BWhitfield2@schools.nyc.gov>; Williams Angela <AWillia6@schools.nyc.gov>; Williams Audrey <AWillia7@schools.nyc.gov>; Williams Donnette <DWilliams41@schools.nyc.gov>; Wilson Marion <MWilson11@schools.nyc.gov>; Wisker Maria <MWisker@schools.nyc.gov>; \
    Yakubov Nathan <NYakubov@schools.nyc.gov>; Young Darnell <DYoung10@schools.nyc.gov>; Zamore Dena <DZamore@schools.nyc.gov>; Zarate Alexandra <AZarate@schools.nyc.gov>; Zeltser Michelle <MZeltser@schools.nyc.gov>; Zervoulei Devito Kimberly <KZervouleiDevito@schools.nyc.gov>; \
    Floyd Nichole (75X811) <NFloyd@schools.nyc.gov>; Brown Tiffany <TBrown70@schools.nyc.gov>; Mintzer Lisa <LMintze@schools.nyc.gov>; Ehrenberg Debra <DEhrenberg@schools.nyc.gov>; MMcCall@schools.nyc.gov;'