import json
breeds_api = {
    'affenpinscher':
        {'male': {'height': '25-30 см', 'weight': '4-6 кг', 'life_span': '12-14 лет', 'origin': 'Германия', 'temperament': 'игривая, уверенная в себе и озорная порода со смелым и любопытным характером.', },
         'female': {'height': '25-30 см', 'weight': '4-6 кг', 'life_span': '12-14 лет', 'origin': 'Германия', 'temperament': 'игривая, уверенная в себе и озорная порода со смелым и любопытным характером.', }},
    'afghan_hound':
        {'male': {'height': '61–73 см', 'weight': '20–27 кг', 'life_span': '13–17 лет', 'origin': 'Авганистан', 'temperament': 'Независимость, отчужденность и царственность в поведении.', },
         'female': {'height': '61–73 см', 'weight': '20–27 кг', 'life_span': '13–17 лет', 'origin': 'Авганистан', 'temperament': 'Независимость, отчужденность и царственность в поведении.', }},
    'african_hunting_dog':
        {'male': {'height': '60-75 см', 'weight': '20-25 кг', 'life_span': '10-13 лет', 'origin': 'Африка', 'temperament': 'Хищная порода не приспособленны к жизни с людьми', },
         'female': {'height': '55-70 см', 'weight': '18.5-23 кг', 'life_span': '10-13 лет', 'origin': 'Африка ', 'temperament': 'Хищная порода не приспособленны к жизни с людьми', }},
    'airedale':
        {'male': {'height': '(58–61 см', 'weight': '18–23 кг', 'life_span': '10-12 лет', 'origin': 'Англия', 'temperament': 'Они умны, энергичны и преданны своим владельцам.', },
         'female': {'height': '56–58 см', 'weight': '16–18 кг', 'life_span': '10-12 лет', 'origin': 'Англия', 'temperament': 'Они умны, энергичны и преданны своим владельцам.', }},
    'american_staffordshire_terrier':
        {'male': {'height': '43–48 см', 'weight': '23–36 кг', 'life_span': '12-16 лет', 'origin': 'Америка', 'temperament': ':умные, уверенные в себе, добродушные, верные и заслуживающие доверия.', },
         'female': {'height': '43–48 см', 'weight': '23–36 кг', 'life_span': '12-16 лет', 'origin': 'Америка', 'temperament': ':умные, уверенные в себе, добродушные, верные и заслуживающие доверия.', }},
    'appenzeller':
        {'male': {'height': '52–56 см', 'weight': '25–32', 'life_span': '12–14 лет', 'origin': 'Швейцария', 'temperament': 'живой, энергичный и спортивный пес, подозрительный к незнакомцам.', },
         'female': {'height': '50–54', 'weight': '22–28', 'life_span': '12–14 лет', 'origin': 'Швейцария', 'temperament': 'живой, энергичный и спортивный пес, подозрительный к незнакомцам.', }},
    'australian_terrier':
        {'male': {'height': '22-28 см', 'weight': '5-7 кг', 'life_span': '12-14 лет', 'origin': 'Австралия', 'temperament': 'умная, энергичная и ласковая порода', },
         'female': {'height': '22-28 см', 'weight': '5-7 кг', 'life_span': '12-14 лет', 'origin': 'Австралия', 'temperament': 'умная, энергичная и ласковая порода', }},
    'basenji':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'basset':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'beagle':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'bedlington_terrier':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'bernese_mountain_dog':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'black-and-tan_coonhound':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'blenheim_spaniel':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'bloodhound':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'bluetick':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'border_collie':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'border_terrier':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'borzoi':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'boston_bull':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'bouvier_des_flandres':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'boxer':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'brabancon_griffon':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'briard':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'brittany_spaniel':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'bull_mastiff':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'cairn':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'cardigan':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'chesapeake_bay_retriever':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'chihuahua':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'chow':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'clumber':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'cocker_spaniel':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'collie':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'curly-coated_retriever':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'dandie_dinmont':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'dhole':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'dingo':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'doberman':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'english_foxhound':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'english_setter':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'english_springer':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'entlebucher':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'eskimo_dog':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'flat-coated_retriever':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'french_bulldog':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'german_shepherd':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'german_short-haired_pointer':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'giant_schnauzer':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'golden_retriever':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'gordon_setter':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'great_dane':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'great_pyrenees':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'greater_swiss_mountain_dog':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'groenendael':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'ibizan_hound':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'irish_setter':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'irish_terrier':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'irish_water_spaniel':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'irish_wolfhound':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'italian_greyhound':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'japanese_spaniel':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'keeshond':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'kelpie':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'kerry_blue_terrier':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'komondor':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'kuvasz':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'labrador_retriever':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'lakeland_terrier':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'leonberg':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'lhasa':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'malamute':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'malinois':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'maltese_dog':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'mexican_hairless':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'miniature_pinscher':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'miniature_poodle':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'miniature_schnauzer':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'newfoundland':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'norfolk_terrier':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'norwegian_elkhound':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'norwich_terrier':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'old_english_sheepdog':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'otterhound':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'papillon':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'pekinese':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'pembroke':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'pomeranian':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'pug':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'redbone':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'rhodesian_ridgeback':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'rottweiler':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'saint_bernard':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'saluki':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'samoyed':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'schipperke':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'scotch_terrier':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'scottish_deerhound':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'sealyham_terrier':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'shetland_sheepdog':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'shih-tzu':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'siberian_husky':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'silky_terrier':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'soft-coated_wheaten_terrier':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'staffordshire_bullterrier':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'standard_poodle':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'standard_schnauzer':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'sussex_spaniel':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'tibetan_mastiff':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'tibetan_terrier':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'toy_poodle':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'toy_terrier':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'vizsla':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'walker_hound':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'weimaraner':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'welsh_springer_spaniel':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'west_highland_white_terrier':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'whippet':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'wire-haired_fox_terrier':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }},
    'yorkshire_terrier':
        {'male': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', },
         'female': {'height': '', 'weight': '', 'life_span': '', 'origin': '', 'temperament': '', }}
}
if __name__ == '__main__':
    r = json.dumps(breeds_api)
    print(r)