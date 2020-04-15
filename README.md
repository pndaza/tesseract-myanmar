# Tesseract Myanmar

Myanmar script အတွက် tesseract OCR ရဲ့ out of the box ပေးထားတဲ့ traineddata ဖိုင်ဟာ 

- ( ၌၊ ၍၊ ၏၊ ၎) နှင့် (ပုဒ်ထီး၊ ပုဒ်မ) အက္ခရာတို့ မပါဘဲ ဖြစ်နေတာကြောင့်
- ဖွန့်အမျိုးအစားများစွာအတွက် training မလုပ်ထားတာကြောင့်
- training text ထဲမှာ zawgyi encoded စာတွေ ရောနှောနေတာကြောင့်

error rate အရမ်းများပါတယ်။

မြန်မာစာအတွက် ocr  အမှန်ဆုံးလို့ ဆို့ရမယ့် google vision ရဲ့ ocr ကလည်း မြန်မာဝေါဟာရအတွက်ဘဲ အဆင်ပြေတယ်။ ပါဠိဝေါဟာရများအတွက် error rate အရမ်းများနေသေးတယ်။

ပါဠိ၊ အဋ္ဌကထာ၊ ဋီကာ နိဿယများကို scan version မှ text version သို့ စွမ်းနိုင်သလောက် ပြောင်းထားဘို့ စိတ်ကူးပေါ်တုန်း tesseract ocr  ရဲ့ myanmar script အတွက် trainneddata ဖိုင်ကို layer replacing နည်းဖြင့် fine tune လုပ်ပြီး စမ်းကြည့်တာ အတော်လေး ရလာဒ်ကောင်းမွန်တာမို့ ပြန်လည်ဝေမျှလိုက်ပါသည်။ error rate ကို ဇယားမှာ ကြည့်ပါ။

မှတ်ချက်။ ။ accuracy အတော်ကောင်းပါသော်လည်း tesseract OCR ၏ text-line finding သည် ဗျည်းထက်၌ ရှိသော လုံးကြီးတင်၊ လုံးကြီးတင်ဆံခတ်၊ အသတ်စသည်တို့သည် ဗျည်းနှင့် မထိစပ်ဘဲ လွတ်နေသော စာလုံးဒီဇိုင်းမျိုးဖြစ်ပါက ထိုလုံးကြီးတင်စသည်တို့ကို လိုင်းတလိုင်းအနေဖြင့် ခွဲထုတ်သောကြောင့် အချို့သော မြန်မာဖွန့်ဒီဇိုင်းများအတွက် မမှန်ပါ။ (  အာရေဗျ၊ ဂျပန်၊ ဂျာမနီ စသည်တို့အတွက်လည်း မမှန်သေး၏ ဟု ဆိုကြ) ။ 



ဒါကတော့ noise မပါတဲ့ eval data set ပေါ်မှာ evaluate လုပ်ထားတာပါ။ noise စသည်ပါလာရင်တော့ ဒီထက်ပိုပြီး error rate များပါလိမ့်မယ်။

| font                                   | char error rate | word error rate |
| :------------------------------------- | --------------- | --------------- |
| Myanmar_PaOh                           | 0.42941127      | 4.3377578       |
| Myanmar_Ethnic_Sans                    | 0.46718541      | 4.4345238       |
| Myanmar_Yein                           | 0.6053413       | 5.8825121       |
| Myanmar_Sans_Pro                       | 0.63756975      | 5.4966313       |
| Myanmar_UI                             | 0.63978621      | 5.8351371       |
| Pyidaungsu                             | 0.68607731      | 5.9856023       |
| MUA_Office                             | 0.70245574      | 6.7455202       |
| Myanmar_Tagu                           | 0.70260465      | 7.8238946       |
| Myanmar_Sabae                          | 0.72382359      | 4.8816138       |
| Noto_Sans_Myanmar                      | 0.73380574      | 5.7155067       |
| Myanmar_MUA                            | 0.74944535      | 6.5346529       |
| Pyidaungsu_Bold                        | 0.76580684      | 7.2995682       |
| Myanmar_Pangram                        | 0.81070258      | 6.2678314       |
| Myanmar_Grand                          | 0.81442107      | 6.0077483       |
| Myanmar_Squarehand                     | 0.82573218      | 7.8014958       |
| Myanmar_Sagar                          | 0.83168089      | 6.2852262       |
| Padauk_Bold                            | 0.87910899      | 8.6717926       |
| Padauk                                 | 0.88295635      | 7.7363192       |
| Noto_Sans_Myanmar_UI                   | 0.90406301      | 6.977467        |
| Myanmar_Sanpya                         | 0.90629666      | 6.7556471       |
| KhunPaOh                               | 0.93467255      | 10.175707       |
| Hopong                                 | 0.9837311       | 7.7665043       |
| ThanLwin                               | 0.98857813      | 7.5042972       |
| Myanmar_Text                           | 0.99648591      | 5.7332251       |
| Ours-Unicode                           | 1.053145        | 7.3451244       |
| Myanmar_Pauklay                        | 1.0548857       | 7.8954101       |
| Myanmar_Ekaya                          | 1.0671492       | 7.4526902       |
| Cherry_Unicode                         | 1.0777003       | 7.1956848       |
| Hsi_Hseng                              | 1.1190725       | 10.013299       |
| Myanmar_Square                         | 1.1897668       | 9.5039683       |
| Myanmar_Gantgaw                        | 1.2558542       | 7.7054364       |
| Myanmar_Chatu                          | 1.3166145       | 10.894742       |
| Myanmar_Phiksel_Smooth                 | 1.3338799       | 12.17939        |
| Myanmar_Taungthu                       | 1.3414034       | 10.334584       |
| Myanmar_Katkuu                         | 1.4077546       | 10.765435       |
| Myanmar_BoKaow                         | 1.4745422       | 10.716612       |
| Myanmar_Waitzar                        | 1.4890937       | 12.193301       |
| Myanmar_Phetsot                        | 1.5279923       | 12.255201       |
| Myanmar_four                           | 1.7663877       | 12.963214       |
| Myanmar_Nayone                         | 1.9427612       | 13.551888       |
| Noto_Sans_Myanmar_Bold                 | 1.9637489       | 13.091575       |
| tawzin ( scan image )                  | 2.0036169       | 5.4761          |
| alankar ( scan image )                 | 2.1429148       | 20.204365       |
| Yunghkio                               | 2.157214        | 9.1917768       |
| Myanmar_Chatu_Light                    | 2.1715123       | 13.758966       |
| Noto_Serif_Myanmar                     | 2.2559152       | 13.520698       |
| monotype_eval_1                        | 2.4217351       | 16.954887       |
| Myanmar_Sketch                         | 2.5663688       | 12.084607       |
| monotype_eval_2                        | 2.57996         | 19.210526       |
| Myanmar_Square_Light                   | 2.76287         | 16.257971       |
| Myanmar_Njaun                          | 2.7668908       | 13.564779       |
| Myanmar_Tagaung                        | 2.9754883       | 19.844419       |
| Yangon                                 | 3.4642327       | 45.052338       |
| buddhavan ( scan image )               | 3.8319597       | 27.555556       |
| YoeYar-One                             | 3.8710353       | 27.79239        |
| buddhavan_medain_filter ( scan image ) | 4.0060693       | 26.222222       |
| Myanmar_Text_Bold                      | 4.0489174       | 10.442834       |
| Myanmar_Taunggyi                       | 4.1705694       | 28.81169        |
| Myanmar_Khway                          | 4.6355567       | 24.030112       |
| salin ( scan image )                   | 4.9816442       | 26.211735       |
| maeu ( scan image )                    | 5.920616        | 26.839827       |
| Myanmar_Handwriting                    | 18.287787       | 46.761013       |







