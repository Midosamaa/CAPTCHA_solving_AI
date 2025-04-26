import os
import random
import string
from PIL import Image, ImageDraw, ImageFont

def get_font_paths():
    # Base font directory
    base_dir = "/usr/share/fonts/captcha_fonts"
    
    # List to store paths of all compatible .ttf fonts
    font_list = []
    broken_fonts = [
    ]
    # "/usr/share/fonts/truetype/samyak/Samyak-Devanagari.ttf",
    # "/usr/share/fonts/truetype/droid/DroidSansFallbackFull.ttf",
    # "/usr/share/fonts/truetype/libreoffice/opens___.ttf",
    # "/usr/share/fonts/truetype/Gubbi/Gubbi.ttf",
    # "/usr/share/fonts/truetype/sinhala/lklug.ttf",
    # "/usr/share/fonts/truetype/teluguvijayam/Ponnala.ttf",
    # "/usr/share/fonts/truetype/teluguvijayam/LakkiReddy.ttf",
    # "/usr/share/fonts/truetype/kacst/KacstDigital.ttf",
    # "/usr/share/fonts/truetype/kacst/KacstPen.ttf",
    # "/usr/share/fonts/truetype/kacst/KacstTitle.ttf",
    # "/usr/share/fonts/truetype/kacst/KacstTitleL.ttf",
    # "/usr/share/fonts/truetype/kacst/KacstFarsi.ttf",
    # "/usr/share/fonts/truetype/kacst/KacstPoster.ttf",
    # "/usr/share/fonts/truetype/kacst/KacstDecorative.ttf",
    # "/usr/share/fonts/truetype/kacst/KacstScreen.ttf",
    # "/usr/share/fonts/truetype/kacst/KacstOffice.ttf",
    # "/usr/share/fonts/truetype/kacst/KacstBook.ttf",
    # "/usr/share/fonts/truetype/kacst/KacstArt.ttf",
    # "/usr/share/fonts/truetype/kacst/KacstQurn.ttf",
    # "/usr/share/fonts/truetype/kacst/KacstLetter.ttf",
    # "/usr/share/fonts/truetype/kacst/mry_KacstQurn.ttf",
    # "/usr/share/fonts/truetype/kacst/KacstNaskh.ttf",
    # "/usr/share/fonts/truetype/malayalam/RaghuMalayalamSans-Regular.ttf",
    # "/usr/share/fonts/truetype/teluguvijayam/RaviPrakash.ttf",
    # "/usr/share/fonts/truetype/Navilu/Navilu.ttf",
    # "/usr/share/fonts/truetype/noto/*.ttf,"
    # "/usr/share/fonts/truetype/noto/NotoSansNushu-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansBuhid-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansKaithi-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansTifinaghGhat-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansMono-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSerifArmenian-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSerifKhojki-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansEthiopic-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSerifTelugu-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansHebrew-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansTifinaghAzawagh-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSerifArmenian-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansTifinagh-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansRejang-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansKhmer-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansGurmukhi-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSans-BoldItalic.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansTakri-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansTifinaghRhissaIxa-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansPauCinHau-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSerifAhom-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansJavanese-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansMeeteiMayek-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansSymbols-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSerif-BoldItalic.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansKhudawadi-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansSiddham-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSerifGurmukhi-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansUgaritic-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansManichaean-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansLepcha-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansRunic-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansWancho-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansSymbols-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansTamil-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansKannada-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSerifTelugu-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSerifGurmukhi-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansTifinaghHawad-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansBamum-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansAdlam-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansSoraSompeng-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoNaskhArabic-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansMarchen-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansOldPersian-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansHanifiRohingya-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSerifBengali-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansTamilSupplement-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansLimbu-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansOlChiki-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansGeorgian-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSerifBalinese-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansKhmer-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansGujarati-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansImperialAramaic-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansPsalterPahlavi-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansArabic-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansThai-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansTifinaghSIL-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansMeeteiMayek-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansOldSogdian-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansBuginese-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansGlagolitic-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansSoraSompeng-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSerifTamil-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoNastaliqUrdu-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansOldHungarian-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansTifinaghAhaggar-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansCham-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSerifDevanagari-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansLinearA-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansArmenian-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansThaana-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansNewa-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansLao-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoTraditionalNushu-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansCherokee-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansGujarati-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansEgyptianHieroglyphs-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansLisu-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSerif-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansElbasan-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSerifMalayalam-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansElymaic-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansBassaVah-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSerifThai-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSerifKhmer-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansTifinaghAgrawImazighen-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansCanadianAboriginal-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansSinhala-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansCypriot-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSerifLao-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSerifNyiakengPuachueHmong-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansJavanese-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSerifTibetan-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansOlChiki-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansDevanagari-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansEthiopic-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoMusic-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSerifMyanmar-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansPahawhHmong-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansMultani-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansCanadianAboriginal-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSerifThai-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSans-Italic.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansOsmanya-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSerifGrantha-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansBrahmi-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansDisplay-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansMath-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansSyriac-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSerifNyiakengPuachueHmong-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansMedefaidrin-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansHanunoo-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansMro-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSerifKannada-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansTaiViet-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSerifLao-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSerifTamil-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansTelugu-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSerifDisplay-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansMongolian-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSerifYezidi-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansBengali-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansLao-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansSinhala-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansBalinese-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansGrantha-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSerifTamilSlanted-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansMasaramGondi-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSerifMalayalam-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansOldItalic-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansAdlamUnjoined-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansMalayalam-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoNastaliqUrdu-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansMahajani-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansHanifiRohingya-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansSaurashtra-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansTifinaghAPT-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansOldTurkic-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSerifDevanagari-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSerifKannada-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansDisplay-BoldItalic.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansDisplay-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansTamil-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSerifDogra-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSerifDisplay-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansTifinaghAdrar-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansKannada-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansThaana-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansSogdian-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansMandaic-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansVai-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoLoopedLao-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansArmenian-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansSymbols2-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSerif-Italic.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansAdlam-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansCaucasianAlbanian-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansMono-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansWarangCiti-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansMedefaidrin-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansKhojki-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansTirhuta-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansNKo-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansDisplay-Italic.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansTaiLe-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansLycian-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansSundanese-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansKayahLi-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansOgham-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansMyanmar-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSerifGeorgian-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansCham-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansOsage-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSerifYezidi-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSerifDisplay-Italic.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansGunjalaGondi-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansSoyombo-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansNabataean-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSerifEthiopic-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansIndicSiyaqNumbers-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansTaiTham-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSerifEthiopic-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoRashiHebrew-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansDeseret-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSerifMyanmar-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansNewTaiLue-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansYi-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSerifTamilSlanted-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoMono-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansMendeKikakui-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoLoopedThai-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansBamum-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSerifGujarati-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansGeorgian-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansThai-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSerifTibetan-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSerifSinhala-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansOldPermic-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansAdlamUnjoined-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansLydian-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansAnatolianHieroglyphs-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansPhagsPa-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSerifGeorgian-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansOldSouthArabian-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansDuployan-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansPhoenician-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansChakma-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansMeroitic-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansKayahLi-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansHebrew-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansSylotiNagri-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansZanabazarSquare-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansBatak-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSerifDisplay-BoldItalic.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansSignWriting-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSerifKhojki-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansBhaiksuki-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansInscriptionalPahlavi-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansShavian-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansTelugu-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansHatran-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansCuneiform-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansCoptic-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansKharoshthi-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansLisu-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansOldNorthArabian-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansArabic-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansOriya-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoLoopedLao-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoLoopedThai-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansGurmukhi-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoNaskhArabic-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansMalayalam-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSerifHebrew-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansLinearB-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansCarian-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoRashiHebrew-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansBalinese-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansMayanNumerals-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansMyanmar-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansTagbanwa-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSerifSinhala-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansInscriptionalParthian-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoKufiArabic-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoKufiArabic-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansBengali-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansOriya-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansSharada-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansTaiTham-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansAvestan-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansMiao-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansPalmyrene-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSerifTangut-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansModi-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansDevanagari-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansTifinaghAir-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSerifHebrew-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansCherokee-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansSamaritan-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSerif-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansTagalog-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansSundanese-Bold.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansGothic-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf",
    # "/usr/share/fonts/truetype/noto/NotoSansTifinaghTawellemmet-Regular.ttf",
    # "/usr/share/fonts/truetype/lyx/wasy10.ttf",
    # "/usr/share/fonts/truetype/alee/Guseul.ttf",
    # # "/usr/share/fonts/truetype/lyx/cmmi10.ttf",
    # "/usr/share/fonts/truetype/lyx/eufm10.ttf",
    # "/usr/share/fonts/truetype/lyx/msbm10.ttf",
    # "/usr/share/fonts/truetype/lyx/msam10.ttf",
    # "/usr/share/fonts/truetype/lyx/esint10.ttf",
    # "/usr/share/fonts/truetype/lyx/dsrom10.ttf",
    # "/usr/share/fonts/truetype/lyx/stmary10.ttf",
    # # "/usr/share/fonts/truetype/lyx/cmr10.ttf",
    # "/usr/share/fonts/truetype/lyx/cmex10.ttf",
    # "/usr/share/fonts/truetype/lyx/rsfs10.ttf",
    
    # "/usr/share/fonts/truetype/lyx/cmsy10.ttf"]

    
    # Loop over each directory in the base font directory
    for root, dirs, files in os.walk(base_dir):
        if '-' in root:  # Skip directories with a dash in their name
            continue

        for file in files:
            if file.endswith(".ttf"):
                font_path = os.path.join(root, file)
                # Test loading the font to ensure compatibility
                try:
                    ImageFont.truetype(font_path, 20)
                    if font_path not in broken_fonts:
                        font_list.append(font_path)  # Add only if it loads successfully
                except IOError:
                    print(f"Skipping incompatible font: {font_path}")
    
    return font_list

def generate_single_char_captcha_for_each_font(output_dir):
    # Set CAPTCHA dimensions
    width, height = 150, 40  # Dimensions of the CAPTCHA

    # Create directory if it doesn’t exist
    captcha_dir = os.path.join(output_dir, "captchas")
    os.makedirs(captcha_dir, exist_ok=True)

    # Get available fonts
    font_paths = get_font_paths()
    if not font_paths:
        print("No fonts found in the specified directories.")
        return

    # Prepare a log file to record font paths used
    log_file_path = os.path.join(output_dir, "font_usage_log.txt")
    with open(log_file_path, 'w') as log_file:
        for font_path in font_paths:
            # Generate a single random character for the CAPTCHA
            captcha_text = random.choice(string.ascii_letters + string.digits)

            # Randomly select a background color for CAPTCHA (darker for more contrast)
            background_color = (random.randint(0, 50), random.randint(0, 50), random.randint(0, 50))
            image = Image.new('RGB', (width, height), background_color)

            draw = ImageDraw.Draw(image)

            try:
                font = ImageFont.truetype(font_path, 30)  # Use a larger font size for better visibility
            except IOError:
                print(f"Skipping incompatible font: {font_path}")
                continue

            # Log the font used
            log_entry = f"Character '{captcha_text}': Font path - {font_path}\n"
            log_file.write(log_entry)

            # Draw the character in the center of the CAPTCHA
            char_color = (random.randint(150, 255), random.randint(150, 255), random.randint(150, 255))
            bbox = draw.textbbox((0, 0), captcha_text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            text_x = (width - text_width) // 2
            text_y = (height - text_height) // 2
            draw.text((text_x, text_y), captcha_text, font=font, fill=char_color)

            # Save the CAPTCHA image with a name that includes the font
            font_name = os.path.basename(font_path).replace('.ttf', '')
            captcha_file_name = f"{captcha_text}_{font_name}.png"
            image.save(os.path.join(captcha_dir, captcha_file_name))

            print(f"Generated CAPTCHA '{captcha_file_name}' using font: {font_path}")

    print(f"Font usage logged in {log_file_path}")

# Define the output directory where CAPTCHAs will be saved
output_directory = "/home/midosama/Desktop/CAPTCHA_solving_AI/fonts"

# Generate a single-character CAPTCHA for each font
generate_single_char_captcha_for_each_font(output_dir=output_directory)