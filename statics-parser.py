from bs4 import BeautifulSoup as bf
from lxml import html  
import requests
import json
from pymongo import MongoClient

def history_dividend_parser(ticker):
    print("start "+ticker)
    url = "https://finance.yahoo.com/quote/%s.HK/history?period1=946857600&period2=1587772800&interval=1d&filter=history&frequency=1d"%(ticker)
    response = requests.get(url, verify=False)
    dividend_start_pos = response.text.find("\"eventsData\"")
    dividend_end_pos = response.text.find("]}", dividend_start_pos)
    dividend_str = response.text[dividend_start_pos:dividend_end_pos+1]
    dividend = json.loads("{"+dividend_str+"}")
    dividend["symbol"] = ticker + ".HK"
    return dividend

def symbol_statics_parser(ticker):
    print("start "+ticker)
    staticmap = {}
    url = "https://finance.yahoo.com/quote/%s/key-statistics?p=%s"%(ticker, ticker)
    response = requests.get(url, verify=False)
    sp = bf(response.text, features="lxml")
    tables = sp.find_all("table")
    for tb in tables:
        rows = tb.findChildren(['th', 'tr'])
        for row in rows:
            cells = row.findChildren('td')
            for cell in cells:
                for s in cell.strings:
                    if s is not None and "Forward Annual Dividend Yield" in s:
                        staticmap["Forward Annual Dividend Yield"]= cells[len(cells)-1].string
                    if s is not None and "Payout Ratio" in s:
                        staticmap["Payout Ratio"]= cells[len(cells)-1].string
                    if s is not None and "52 Week High" in s:
                        staticmap["52 Week High"]= cells[len(cells)-1].string
                    if s is not None and "52 Week Low" in s:
                        staticmap["52 Week Low"]= cells[len(cells)-1].string
                    if s is not None and "Diluted EPS (ttm)" in s:
                        staticmap["Diluted EPS (ttm)"]= cells[len(cells)-1].string
                    if s is not None and "Ex-Dividend Date" in s:
                        staticmap["Ex-Dividend Date"]= cells[len(cells)-1].string
    return staticmap 
    

symbol_list = ["00001",
"00002",
"00003",
"00004",
"00005",
"00006",
"00007",
"00008",
"00009",
"00010",
"00011",
"00012",
"00014",
"00015",
"00016",
"00017",
"00018",
"00019",
"00020",
"00021",
"00022",
"00023",
"00024",
"00025",
"00026",
"00027",
"00028",
"00029",
"00030",
"00031",
"00032",
"00033",
"00034",
"00035",
"00036",
"00037",
"00038",
"00039",
"00040",
"00041",
"00042",
"00043",
"00045",
"00046",
"00047",
"00048",
"00050",
"00051",
"00052",
"00053",
"00055",
"00056",
"00057",
"00058",
"00059",
"00060",
"00061",
"00062",
"00063",
"00064",
"00065",
"00066",
"00067",
"00068",
"00069",
"00070",
"00071",
"00072",
"00073",
"00075",
"00076",
"00077",
"00078",
"00079",
"00081",
"00082",
"00083",
"00084",
"00085",
"00086",
"00087",
"00088",
"00089",
"00090",
"00091",
"00092",
"00093",
"00094",
"00095",
"00096",
"00097",
"00098",
"00099",
"00100",
"00101",
"00102",
"00103",
"00104",
"00105",
"00106",
"00107",
"00108",
"00109",
"00110",
"00111",
"00112",
"00113",
"00114",
"00115",
"00116",
"00117",
"00118",
"00119",
"00120",
"00122",
"00123",
"00124",
"00125",
"00126",
"00127",
"00128",
"00129",
"00130",
"00131",
"00132",
"00135",
"00136",
"00137",
"00138",
"00139",
"00141",
"00142",
"00143",
"00144",
"00145",
"00146",
"00147",
"00148",
"00149",
"00150",
"00151",
"00152",
"00153",
"00154",
"00155",
"00156",
"00157",
"00158",
"00159",
"00160",
"00161",
"00162",
"00163",
"00164",
"00165",
"00166",
"00167",
"00168",
"00169",
"00171",
"00172",
"00173",
"00174",
"00175",
"00176",
"00177",
"00178",
"00179",
"00180",
"00181",
"00182",
"00183",
"00184",
"00185",
"00186",
"00187",
"00188",
"00189",
"00190",
"00191",
"00193",
"00194",
"00195",
"00196",
"00197",
"00198",
"00199",
"00200",
"00201",
"00202",
"00205",
"00206",
"00207",
"00208",
"00209",
"00210",
"00211",
"00212",
"00213",
"00214",
"00215",
"00216",
"00217",
"00218",
"00219",
"00220",
"00221",
"00222",
"00223",
"00224",
"00225",
"00226",
"00227",
"00228",
"00229",
"00230",
"00231",
"00232",
"00234",
"00235",
"00236",
"00237",
"00238",
"00239",
"00240",
"00241",
"00242",
"00243",
"00244",
"00245",
"00247",
"00248",
"00250",
"00251",
"00252",
"00253",
"00254",
"00255",
"00256",
"00257",
"00258",
"00259",
"00260",
"00261",
"00262",
"00263",
"00264",
"00265",
"00266",
"00267",
"00268",
"00269",
"00270",
"00271",
"00272",
"00273",
"00274",
"00275",
"00276",
"00277",
"00278",
"00279",
"00280",
"00281",
"00282",
"00285",
"00286",
"00287",
"00288",
"00289",
"00290",
"00291",
"00292",
"00293",
"00294",
"00295",
"00296",
"00297",
"00298",
"00299",
"00301",
"00302",
"00303",
"00305",
"00306",
"00307",
"00308",
"00309",
"00311",
"00312",
"00313",
"00315",
"00316",
"00317",
"00318",
"00320",
"00321",
"00322",
"00323",
"00326",
"00327",
"00328",
"00329",
"00330",
"00331",
"00332",
"00333",
"00334",
"00335",
"00336",
"00337",
"00338",
"00340",
"00341",
"00342",
"00343",
"00345",
"00346",
"00347",
"00348",
"00351",
"00352",
"00353",
"00354",
"00355",
"00357",
"00358",
"00359",
"00360",
"00361",
"00362",
"00363",
"00364",
"00365",
"00366",
"00367",
"00369",
"00370",
"00371",
"00372",
"00373",
"00374",
"00375",
"00376",
"00377",
"00378",
"00379",
"00380",
"00381",
"00382",
"00383",
"00384",
"00385",
"00386",
"00387",
"00388",
"00389",
"00390",
"00391",
"00392",
"00393",
"00395",
"00396",
"00397",
"00398",
"00399",
"00400",
"00401",
"00402",
"00403",
"00406",
"00408",
"00410",
"00411",
"00412",
"00413",
"00416",
"00417",
"00418",
"00419",
"00420",
"00422",
"00423",
"00425",
"00426",
"00430",
"00431",
"00432",
"00433",
"00434",
"00436",
"00438",
"00439",
"00440",
"00442",
"00444",
"00445",
"00449",
"00450",
"00451",
"00455",
"00456",
"00458",
"00459",
"00460",
"00462",
"00464",
"00465",
"00467",
"00468",
"00469",
"00471",
"00472",
"00474",
"00475",
"00476",
"00479",
"00480",
"00482",
"00483",
"00484",
"00485",
"00486",
"00487",
"00488",
"00489",
"00491",
"00493",
"00494",
"00495",
"00496",
"00497",
"00498",
"00499",
"00500",
"00503",
"00505",
"00506",
"00508",
"00509",
"00510",
"00511",
"00512",
"00513",
"00515",
"00517",
"00518",
"00519",
"00520",
"00521",
"00522",
"00524",
"00525",
"00526",
"00527",
"00528",
"00529",
"00530",
"00531",
"00532",
"00533",
"00535",
"00536",
"00538",
"00539",
"00540",
"00542",
"00543",
"00544",
"00546",
"00547",
"00548",
"00550",
"00551",
"00552",
"00553",
"00554",
"00555",
"00556",
"00557",
"00558",
"00559",
"00560",
"00563",
"00564",
"00565",
"00567",
"00568",
"00570",
"00571",
"00572",
"00573",
"00574",
"00575",
"00576",
"00577",
"00578",
"00579",
"00580",
"00581",
"00582",
"00583",
"00585",
"00586",
"00587",
"00588",
"00589",
"00590",
"00591",
"00592",
"00593",
"00595",
"00596",
"00598",
"00599",
"00600",
"00601",
"00602",
"00603",
"00604",
"00605",
"00607",
"00608",
"00609",
"00610",
"00611",
"00613",
"00616",
"00617",
"00618",
"00619",
"00620",
"00621",
"00622",
"00623",
"00626",
"00627",
"00628",
"00629",
"00630",
"00631",
"00632",
"00633",
"00635",
"00636",
"00637",
"00638",
"00639",
"00640",
"00641",
"00643",
"00645",
"00646",
"00647",
"00648",
"00650",
"00651",
"00653",
"00655",
"00656",
"00657",
"00658",
"00659",
"00660",
"00661",
"00662",
"00663",
"00665",
"00667",
"00668",
"00669",
"00670",
"00672",
"00673",
"00674",
"00675",
"00676",
"00677",
"00678",
"00679",
"00680",
"00681",
"00682",
"00683",
"00684",
"00685",
"00686",
"00687",
"00688",
"00689",
"00690",
"00691",
"00693",
"00694",
"00695",
"00696",
"00697",
"00698",
"00699",
"00700",
"00701",
"00702",
"00703",
"00704",
"00706",
"00707",
"00708",
"00709",
"00710",
"00711",
"00712",
"00713",
"00715",
"00716",
"00717",
"00718",
"00719",
"00720",
"00722",
"00723",
"00724",
"00725",
"00726",
"00727",
"00728",
"00729",
"00730",
"00731",
"00732",
"00733",
"00736",
"00737",
"00738",
"00743",
"00745",
"00746",
"00747",
"00750",
"00751",
"00752",
"00753",
"00754",
"00755",
"00756",
"00757",
"00758",
"00759",
"00760",
"00762",
"00763",
"00764",
"00765",
"00766",
"00767",
"00769",
"00771",
"00772",
"00775",
"00776",
"00777",
"00780",
"00784",
"00787",
"00788",
"00789",
"00794",
"00797",
"00798",
"00799",
"00800",
"00801",
"00802",
"00803",
"00804",
"00806",
"00807",
"00809",
"00811",
"00812",
"00813",
"00814",
"00815",
"00816",
"00817",
"00818",
"00819",
"00821",
"00822",
"00825",
"00826",
"00827",
"00828",
"00829",
"00830",
"00831",
"00832",
"00833",
"00834",
"00836",
"00837",
"00838",
"00839",
"00840",
"00841",
"00842",
"00844",
"00845",
"00846",
"00848",
"00850",
"00851",
"00852",
"00853",
"00854",
"00855",
"00856",
"00857",
"00858",
"00859",
"00860",
"00861",
"00862",
"00863",
"00864",
"00865",
"00866",
"00867",
"00868",
"00869",
"00871",
"00872",
"00874",
"00875",
"00876",
"00877",
"00878",
"00880",
"00881",
"00882",
"00883",
"00884",
"00885",
"00886",
"00887",
"00888",
"00889",
"00891",
"00893",
"00894",
"00895",
"00896",
"00897",
"00898",
"00899",
"00900",
"00902",
"00904",
"00906",
"00907",
"00908",
"00910",
"00911",
"00912",
"00914",
"00915",
"00916",
"00918",
"00919",
"00921",
"00922",
"00923",
"00924",
"00925",
"00926",
"00927",
"00928",
"00929",
"00931",
"00932",
"00933",
"00934",
"00935",
"00936",
"00938",
"00939",
"00941",
"00943",
"00945",
"00947",
"00948",
"00950",
"00951",
"00952",
"00953",
"00954",
"00956",
"00959",
"00960",
"00966",
"00967",
"00968",
"00969",
"00970",
"00973",
"00974",
"00975",
"00976",
"00978",
"00979",
"00980",
"00981",
"00982",
"00983",
"00984",
"00985",
"00986",
"00987",
"00988",
"00989",
"00990",
"00991",
"00992",
"00993",
"00994",
"00995",
"00996",
"00997",
"00998",
"00999",
"01000",
"01001",
"01002",
"01003",
"01004",
"01005",
"01006",
"01007",
"01008",
"01009",
"01010",
"01011",
"01013",
"01019",
"01020",
"01022",
"01023",
"01025",
"01026",
"01027",
"01028",
"01029",
"01030",
"01031",
"01033",
"01034",
"01035",
"01036",
"01037",
"01038",
"01039",
"01041",
"01043",
"01044",
"01045",
"01046",
"01047",
"01049",
"01050",
"01051",
"01052",
"01053",
"01055",
"01057",
"01058",
"01059",
"01060",
"01061",
"01063",
"01064",
"01065",
"01066",
"01068",
"01069",
"01070",
"01071",
"01072",
"01073",
"01075",
"01076",
"01079",
"01080",
"01082",
"01083",
"01084",
"01085",
"01086",
"01087",
"01088",
"01089",
"01090",
"01091",
"01093",
"01094",
"01096",
"01097",
"01098",
"01099",
"01100",
"01101",
"01102",
"01103",
"01104",
"01105",
"01106",
"01107",
"01108",
"01109",
"01110",
"01111",
"01112",
"01113",
"01114",
"01115",
"01116",
"01117",
"01118",
"01119",
"01120",
"01121",
"01122",
"01123",
"01124",
"01125",
"01126",
"01127",
"01128",
"01129",
"01130",
"01131",
"01132",
"01133",
"01134",
"01137",
"01138",
"01139",
"01141",
"01142",
"01143",
"01145",
"01146",
"01148",
"01150",
"01151",
"01152",
"01155",
"01157",
"01158",
"01159",
"01161",
"01164",
"01165",
"01166",
"01168",
"01169",
"01170",
"01171",
"01172",
"01173",
"01175",
"01176",
"01177",
"01178",
"01180",
"01181",
"01182",
"01183",
"01184",
"01185",
"01186",
"01188",
"01189",
"01190",
"01191",
"01192",
"01193",
"01194",
"01195",
"01196",
"01198",
"01199",
"01200",
"01201",
"01202",
"01203",
"01205",
"01206",
"01207",
"01208",
"01210",
"01211",
"01212",
"01213",
"01215",
"01216",
"01218",
"01219",
"01220",
"01221",
"01222",
"01223",
"01224",
"01225",
"01228",
"01229",
"01230",
"01231",
"01232",
"01233",
"01234",
"01235",
"01237",
"01238",
"01239",
"01240",
"01241",
"01243",
"01245",
"01246",
"01247",
"01249",
"01250",
"01251",
"01252",
"01253",
"01255",
"01257",
"01258",
"01259",
"01260",
"01262",
"01263",
"01265",
"01266",
"01268",
"01269",
"01270",
"01271",
"01272",
"01273",
"01277",
"01278",
"01280",
"01281",
"01282",
"01283",
"01285",
"01286",
"01288",
"01289",
"01290",
"01292",
"01293",
"01296",
"01297",
"01298",
"01299",
"01300",
"01301",
"01302",
"01303",
"01305",
"01308",
"01310",
"01312",
"01313",
"01314",
"01315",
"01316",
"01317",
"01318",
"01319",
"01321",
"01322",
"01323",
"01326",
"01327",
"01328",
"01329",
"01330",
"01332",
"01333",
"01335",
"01336",
"01337",
"01338",
"01339",
"01340",
"01341",
"01343",
"01345",
"01346",
"01347",
"01348",
"01349",
"01353",
"01355",
"01357",
"01358",
"01359",
"01360",
"01361",
"01362",
"01363",
"01365",
"01366",
"01367",
"01368",
"01369",
"01370",
"01371",
"01372",
"01373",
"01375",
"01378",
"01380",
"01381",
"01382",
"01383",
"01385",
"01386",
"01387",
"01388",
"01389",
"01393",
"01395",
"01396",
"01397",
"01398",
"01399",
"01400",
"01401",
"01402",
"01410",
"01412",
"01415",
"01416",
"01417",
"01418",
"01419",
"01420",
"01421",
"01425",
"01427",
"01428",
"01430",
"01431",
"01432",
"01433",
"01439",
"01442",
"01443",
"01446",
"01447",
"01448",
"01450",
"01451",
"01452",
"01456",
"01458",
"01459",
"01460",
"01461",
"01462",
"01463",
"01466",
"01468",
"01469",
"01470",
"01472",
"01475",
"01476",
"01478",
"01480",
"01483",
"01486",
"01488",
"01492",
"01495",
"01496",
"01498",
"01499",
"01500",
"01501",
"01508",
"01509",
"01513",
"01515",
"01518",
"01520",
"01521",
"01522",
"01523",
"01525",
"01526",
"01527",
"01528",
"01529",
"01530",
"01532",
"01533",
"01536",
"01538",
"01539",
"01540",
"01542",
"01543",
"01545",
"01546",
"01547",
"01548",
"01549",
"01551",
"01552",
"01553",
"01555",
"01556",
"01557",
"01558",
"01559",
"01560",
"01561",
"01563",
"01565",
"01566",
"01568",
"01569",
"01570",
"01571",
"01572",
"01573",
"01575",
"01576",
"01577",
"01578",
"01579",
"01580",
"01581",
"01582",
"01583",
"01585",
"01586",
"01587",
"01588",
"01589",
"01591",
"01592",
"01593",
"01596",
"01598",
"01599",
"01600",
"01601",
"01606",
"01608",
"01609",
"01610",
"01611",
"01612",
"01613",
"01615",
"01616",
"01617",
"01618",
"01619",
"01620",
"01621",
"01622",
"01623",
"01626",
"01627",
"01628",
"01629",
"01630",
"01631",
"01632",
"01633",
"01635",
"01636",
"01637",
"01638",
"01639",
"01640",
"01647",
"01649",
"01651",
"01652",
"01653",
"01655",
"01656",
"01657",
"01658",
"01659",
"01660",
"01661",
"01662",
"01663",
"01665",
"01666",
"01667",
"01668",
"01669",
"01671",
"01672",
"01673",
"01675",
"01676",
"01678",
"01679",
"01680",
"01681",
"01682",
"01683",
"01685",
"01686",
"01689",
"01690",
"01691",
"01692",
"01693",
"01695",
"01696",
"01697",
"01698",
"01699",
"01701",
"01702",
"01703",
"01705",
"01706",
"01707",
"01708",
"01709",
"01710",
"01711",
"01712",
"01713",
"01715",
"01716",
"01717",
"01718",
"01719",
"01720",
"01721",
"01722",
"01723",
"01725",
"01726",
"01727",
"01728",
"01729",
"01730",
"01731",
"01732",
"01733",
"01735",
"01736",
"01737",
"01738",
"01739",
"01740",
"01741",
"01742",
"01743",
"01745",
"01746",
"01747",
"01748",
"01749",
"01750",
"01751",
"01752",
"01753",
"01755",
"01756",
"01757",
"01758",
"01759",
"01760",
"01761",
"01762",
"01763",
"01765",
"01766",
"01767",
"01769",
"01771",
"01772",
"01773",
"01775",
"01776",
"01777",
"01778",
"01780",
"01781",
"01782",
"01783",
"01785",
"01786",
"01787",
"01788",
"01789",
"01790",
"01792",
"01793",
"01796",
"01797",
"01798",
"01799",
"01800",
"01801",
"01802",
"01803",
"01806",
"01808",
"01809",
"01810",
"01811",
"01812",
"01813",
"01815",
"01816",
"01817",
"01818",
"01820",
"01821",
"01822",
"01823",
"01825",
"01826",
"01827",
"01829",
"01830",
"01831",
"01832",
"01833",
"01835",
"01836",
"01837",
"01838",
"01839",
"01841",
"01842",
"01843",
"01845",
"01846",
"01847",
"01848",
"01849",
"01850",
"01851",
"01853",
"01854",
"01856",
"01857",
"01858",
"01859",
"01860",
"01861",
"01862",
"01863",
"01865",
"01866",
"01867",
"01868",
"01869",
"01870",
"01871",
"01872",
"01873",
"01875",
"01876",
"01877",
"01878",
"01882",
"01883",
"01884",
"01885",
"01886",
"01888",
"01889",
"01890",
"01891",
"01894",
"01895",
"01896",
"01897",
"01898",
"01899",
"01900",
"01901",
"01902",
"01903",
"01905",
"01906",
"01907",
"01908",
"01909",
"01910",
"01911",
"01912",
"01913",
"01915",
"01916",
"01917",
"01918",
"01919",
"01920",
"01921",
"01922",
"01925",
"01928",
"01929",
"01930",
"01931",
"01932",
"01933",
"01935",
"01937",
"01938",
"01939",
"01941",
"01943",
"01949",
"01950",
"01951",
"01955",
"01958",
"01959",
"01960",
"01961",
"01962",
"01963",
"01966",
"01967",
"01968",
"01969",
"01970",
"01972",
"01975",
"01977",
"01978",
"01979",
"01980",
"01982",
"01983",
"01985",
"01986",
"01987",
"01988",
"01989",
"01990",
"01991",
"01992",
"01993",
"01995",
"01996",
"01997",
"01998",
"01999",
"02000",
"02001",
"02002",
"02003",
"02005",
"02006",
"02007",
"02008",
"02009",
"02010",
"02011",
"02012",
"02013",
"02014",
"02016",
"02017",
"02018",
"02019",
"02020",
"02022",
"02023",
"02025",
"02028",
"02030",
"02031",
"02033",
"02038",
"02039",
"02048",
"02051",
"02060",
"02066",
"02068",
"02078",
"02080",
"02083",
"02086",
"02088",
"02098",
"02099",
"02100",
"02103",
"02108",
"02111",
"02112",
"02113",
"02116",
"02118",
"02119",
"02120",
"02122",
"02123",
"02128",
"02133",
"02136",
"02138",
"02139",
"02163",
"02166",
"02168",
"02178",
"02180",
"02181",
"02182",
"02183",
"02186",
"02188",
"02189",
"02193",
"02196",
"02198",
"02199",
"02202",
"02203",
"02208",
"02211",
"02212",
"02213",
"02218",
"02221",
"02222",
"02223",
"02225",
"02226",
"02227",
"02228",
"02230",
"02231",
"02232",
"02233",
"02236",
"02238",
"02239",
"02255",
"02258",
"02262",
"02263",
"02266",
"02268",
"02269",
"02277",
"02278",
"02280",
"02281",
"02282",
"02283",
"02286",
"02288",
"02289",
"02292",
"02293",
"02296",
"02298",
"02299",
"02300",
"02302",
"02303",
"02307",
"02308",
"02309",
"02310",
"02313",
"02314",
"02317",
"02318",
"02319",
"02320",
"02322",
"02323",
"02326",
"02327",
"02328",
"02329",
"02330",
"02331",
"02333",
"02336",
"02337",
"02338",
"02339",
"02340",
"02341",
"02342",
"02343",
"02345",
"02346",
"02348",
"02349",
"02355",
"02356",
"02357",
"02358",
"02359",
"02360",
"02362",
"02363",
"02366",
"02368",
"02369",
"02371",
"02377",
"02378",
"02379",
"02380",
"02382",
"02383",
"02386",
"02388",
"02389",
"02393",
"02398",
"02399",
"02400",
"02448",
"02488",
"02500",
"02528",
"02552",
"02558",
"02588",
"02600",
"02601",
"02606",
"02607",
"02608",
"02611",
"02616",
"02623",
"02628",
"02633",
"02638",
"02660",
"02662",
"02663",
"02666",
"02668",
"02669",
"02678",
"02680",
"02682",
"02683",
"02686",
"02688",
"02689",
"02696",
"02698",
"02699",
"02700",
"02708",
"02718",
"02722",
"02727",
"02728",
"02738",
"02768",
"02772",
"02777",
"02779",
"02788",
"02789",
"02798",
"02799",
"02858",
"02863",
"02866",
"02868",
"02869",
"02877",
"02878",
"02880",
"02882",
"02883",
"02885",
"02886",
"02888",
"02892",
"02898",
"02899",
"02906",
"02975",
"02976",
"02985",
"02986",
"02987",
"02988",
"02989",
"02991",
"03300",
"03301",
"03302",
"03303",
"03306",
"03308",
"03309",
"03311",
"03313",
"03315",
"03316",
"03318",
"03319",
"03320",
"03321",
"03322",
"03323",
"03326",
"03328",
"03329",
"03330",
"03331",
"03332",
"03333",
"03335",
"03336",
"03337",
"03339",
"03344",
"03348",
"03358",
"03360",
"03363",
"03366",
"03368",
"03369",
"03377",
"03378",
"03380",
"03382",
"03383",
"03389",
"03393",
"03395",
"03396",
"03398",
"03399",
"03600",
"03601",
"03603",
"03606",
"03608",
"03613",
"03616",
"03618",
"03623",
"03626",
"03628",
"03633",
"03636",
"03638",
"03639",
"03662",
"03663",
"03666",
"03668",
"03669",
"03678",
"03680",
"03681",
"03683",
"03686",
"03688",
"03689",
"03690",
"03692",
"03698",
"03699",
"03700",
"03708",
"03709",
"03718",
"03728",
"03737",
"03738",
"03759",
"03768",
"03773",
"03778",
"03788",
"03789",
"03798",
"03799",
"03800",
"03808",
"03813",
"03816",
"03818",
"03822",
"03828",
"03830",
"03833",
"03836",
"03838",
"03839",
"03848",
"03860",
"03866",
"03868",
"03869",
"03877",
"03878",
"03882",
"03883",
"03886",
"03888",
"03889",
"03893",
"03898",
"03899",
"03900",
"03903",
"03908",
"03918",
"03919",
"03928",
"03933",
"03938",
"03939",
"03948",
"03958",
"03963",
"03966",
"03968",
"03969",
"03978",
"03983",
"03988",
"03989",
"03990",
"03991",
"03992",
"03993",
"03996",
"03997",
"03998",
"03999",
"04604",
"04605",
"04606",
"04607",
"04608",
"04609",
"04610",
"04611",
"04612",
"04613",
"04614",
"04615",
"04616",
"04617",
"04618",
"04619",
"06030",
"06033",
"06036",
"06038",
"06049",
"06055",
"06058",
"06060",
"06066",
"06068",
"06069",
"06080",
"06083",
"06088",
"06090",
"06093",
"06098",
"06099",
"06100",
"06108",
"06110",
"06111",
"06113",
"06116",
"06117",
"06118",
"06119",
"06122",
"06123",
"06128",
"06133",
"06136",
"06138",
"06139",
"06158",
"06160",
"06161",
"06162",
"06163",
"06166",
"06168",
"06169",
"06178",
"06182",
"06183",
"06185",
"06186",
"06188",
"06189",
"06190",
"06193",
"06196",
"06198",
"06199",
"06805",
"06806",
"06808",
"06811",
"06816",
"06818",
"06819",
"06820",
"06822",
"06823",
"06826",
"06828",
"06829",
"06830",
"06833",
"06836",
"06837",
"06838",
"06839",
"06855",
"06858",
"06860",
"06862",
"06865",
"06866",
"06868",
"06869",
"06877",
"06878",
"06880",
"06881",
"06882",
"06885",
"06886",
"06888",
"06889",
"06890",
"06893",
"06896",
"06898",
"06899",
"06908",
"06918",
"06919",
"06928",
"06966",
"09900",
"09909",
"09911",
"09916",
"09918",
"09919",
"09922",
"09928",
"09929",
"09933",
"09936",
"09938",
"09966",
"09968",
"09969",
"09988",
"09998"] 

symbol_list1 = ["06068",
"06069",
"06080",
"06083",
"06088",
"06090",
"06093",
"06098",
"06099",
"06100",
"06108",
"06110",
"06111",
"06113",
"06116",
"06117",
"06118",
"06119",
"06122",
"06123",
"06128",
"06133",
"06136",
"06138",
"06139",
"06158",
"06160",
"06161",
"06162",
"06163",
"06166",
"06168",
"06169",
"06178",
"06182",
"06183",
"06185",
"06186",
"06188",
"06189",
"06190",
"06193",
"06196",
"06198",
"06199",
"06805",
"06806",
"06808",
"06811",
"06816",
"06818",
"06819",
"06820",
"06822",
"06823",
"06826",
"06828",
"06829",
"06830",
"06833",
"06836",
"06837",
"06838",
"06839",
"06855",
"06858",
"06860",
"06862",
"06865",
"06866",
"06868",
"06869",
"06877",
"06878",
"06880",
"06881",
"06882",
"06885",
"06886",
"06888",
"06889",
"06890",
"06893",
"06896",
"06898",
"06899",
"06908",
"06918",
"06919",
"06928",
"06966",
"09900",
"09909",
"09911",
"09916",
"09918",
"09919",
"09922",
"09928",
"09929",
"09933",
"09936",
"09938",
"09966",
"09968",
"09969",
"09988",
"09998"]

def historical_dividend_mongoDB():
    for s in symbol_list:
        dividend = history_dividend_parser(s[1:])
        with open(s+".json", "w") as f:
            json.dump(dividend, f)

def upload_dividend_mongoDB():
    client = MongoClient("mongodb+srv://admin_2020:admin_2020@stockhistoricaldata-brhcu.mongodb.net/test?retryWrites=true&w=majority")
    db=client.hk_equity_hist

    for s in symbol_list:
        with open(s+".json") as f:
            dividend = json.load(f)
            result=db.dividendhist.insert_one(dividend)
            print(s+"Created %s"%result.inserted_id)



if __name__=="__main__":
    upload_dividend_mongoDB()

def comment_func():
    symbol_dict = {}
    for s in symbol_list:
        symbol_dict[s] = symbol_statics_parser(s[1:]+".HK")
        print(symbol_dict[s])

    with open("symbol.json","w") as f:
        json.dump(symbol_dict,f)