import requests
import json
import pandas as pd
import pickle
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu
import base64


def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
        unsafe_allow_html=True
    )
District = [("NICOBAR", "SOUTH ANDAMAN", "N & M ANDAMAN"), (
    "LOHIT", "EAST SIANG", "SUBANSIRI F.D", "TIRAP", "ANJAW (LOHIT)", "LOWER DIBANG", "CHANGLANG", "PAPUM PARE",
    "LOW SUBANSIRI", "UPPER SIANG", "WEST SIANG", "DIBANG VALLEY", "WEST KAMENG", "EAST KAMENG", "TAWANG(W KAME",
    "KURUNG KUMEY"), ("CACHAR", "DARRANG", "GOALPARA", "KAMRUP", "LAKHIMPUR", "NORTH CACHAR", "NAGAON", "SIVASAGAR",
                      "BARPETA", "DHUBRI", "DIBRUGARH", "JORHAT", "KARIMGANJ", "KOKRAJHAR", "SHONITPUR", "GOLAGHAT",
                      "TINSUKIA", "HAILAKANDI", "DHEMAJI(LAKHI", "KARBI ANGLONG", "UDALGURI(DARA", "KAMRUP METROP",
                      "CHIRANG(BONGAI", "BAKSA BARPETA", "BONGAIGAON", "MORIGAON", "NALBARI"), (
                "EAST KHASI HI", "JAINTIA HILLS", "EAST GARO HIL", "RI-BHOI", "SOUTH GARO HI", "W KHASI HILL",
                "WEST GARO HIL"), (
                "IMPHAL EAST", "SENAPATI", "TAMENGLONG", "CHANDEL", "UKHRUL", "THOUBAL", "BISHNUPUR", "IMPHAL WEST",
                "CHURACHANDPUR"),
                ("AIZAWL", "CHAMPHAI", "KOLASIB", "LUNGLEI", "CHHIMTUIPUI", "LAWNGTLAI", "MAMIT", "SAIHA", "SERCHHIP"),
                ("KOHIMA", "TUENSANG", "MOKOKCHUNG", "DIMAPUR", "WOKHA", "MON", "ZUNHEBOTO", "PHEK", "KEPHRIE",
                 "LONGLENG", "PEREN"), ("NORTH TRIPURA", "SOUTH TRIPURA", "WEST TRIPURA", "DHALAI"), (
                "COOCH BEHAR", "DARJEELING", "JALPAIGURI", "MALDA", "SOUTH DINAJPUR", "NORTH DINAJPUR", "BANKURA",
                "BIRBHUM", "BURDWAN", "HOOGHLY", "HOWRAH", "PURULIA", "MURSHIDABAD", "NADIA", "NORTH 24 PARG",
                "SOUTH 24 PARG", "EAST MIDNAPOR", "WEST MIDNAPOR", "KOLKATA"),
                ("NORTH SIKKIM", "EAST SIKKIM", "WEST SIKKIM", "SOUTH SIKKIM"), (
                "BALASORE", "BOLANGIR", "KANDHAMAL/PHU", "CUTTACK", "DHENKANAL", "GANJAM", "KALAHANDI", "KEONDJHARGARH",
                "KORAPUT", "MAYURBHANJ", "PURI", "SAMBALPUR", "SUNDARGARH", "BHADRAK", "JAJPUR", "KENDRAPARA", "ANGUL",
                "NAWAPARA", "MALKANGIRI", "NAWARANGPUR", "NAYAGARH", "KHURDA", "BARGARH", "JHARSUGUDA", "DEOGARH",
                "RAYAGADA", "GAJAPATI", "JAGATSINGHAPU", "BOUDHGARH", "SONEPUR"), (
                "BOKARO", "DHANBAD", "DUMKA", "HAZARIBAG", "PALAMU", "RANCHI", "SAHIBGANJ", "WEST SINGHBHUM", "DEOGHAR",
                "GIRIDIH", "GODDA", "GUMLA", "LOHARDAGA", "CHATRA", "KODERMA", "PAKUR", "EAST SINGHBHU", "GARHWA",
                "SERAIKELA-KHA", "JAMTARA", "LATEHAR", "SIMDEGA", "KHUNTI(RANCHI", "RAMGARH"), (
                "BHAGALPUR", "EAST CHAMPARAN", "DARBHANGA", "GAYA", "MUNGER", "MUZAFFARPUR", "WEST CHAMPARAN", "PURNEA",
                "GOPALGANJ", "MADHUBANI", "AURANGABAD", "BEGUSARAI", "BHOJPUR", "NALANDA", "PATNA", "KATIHAR",
                "KHAGARIA", "SARAN", "MADHEPURA", "NAWADA", "ROHTAS", "SAMASTIPUR", "SITAMARHI", "SIWAN", "VAISHALI",
                "JAHANABAD", "BUXAR", "ARARIA", "BANKA", "BHABUA", "JAMUI", "KISHANGANJ", "SHEIKHPURA", "SUPAUL",
                "LAKHISARAI", "SHEOHAR", "ARWAL", "SAHARSA"), (
                "ALLAHABAD", "AZAMGARH", "BAHRAICH", "BALLIA", "BANDA", "BARABANKI", "BASTI", "DEORIA", "FAIZABAD",
                "FARRUKHABAD", "FATEHPUR", "GHAZIPUR", "GONDA", "GORAKHPUR", "HARDOI", "JAUNPUR", "KANPUR NAGAR",
                "KHERI LAKHIMP", "LUCKNOW", "MIRZAPUR", "PRATAPGARH", "RAE BARELI", "SITAPUR", "SULTANPUR", "UNNAO",
                "VARANASI", "SONBHADRA", "MAHARAJGANJ", "MAU", "SIDDHARTH NGR", "KUSHINAGAR", "AMBEDKAR NAGAR",
                "KANNAUJ", "BALRAMPUR", "KAUSHAMBI", "SAHUJI MAHARA", "KANPUR DEHAT", "CHANDAULI", "SANT KABIR NGR",
                "SANT RAVIDAS", "SHRAVASTI NGR", "AGRA", "ALIGARH", "BAREILLY", "BIJNOR", "BADAUN", "BULANDSHAHAR",
                "ETAH", "ETAWAH", "HAMIRPUR", "JALAUN", "JHANSI", "LALITPUR", "MAINPURI", "MATHURA", "MEERUT",
                "MORADABAD", "MUZAFFARNAGAR", "PILIBHIT", "RAMPUR", "SAHARANPUR", "SHAHJAHANPUR", "GHAZIABAD",
                "FIROZABAD", "MAHOBA", "MAHAMAYA NAGA", "AURAIYA", "BAGPAT", "JYOTIBA PHULE", "GAUTAM BUDDHA",
                "KANSHIRAM NAG"), (
                "ALMORA", "CHAMOLI", "DEHRADUN", "GARHWAL PAURI", "NAINITAL", "PITHORAGARH", "GARHWAL TEHRI",
                "UTTARKASHI", "HARIDWAR", "CHAMPAWAT", "RUDRAPRAYAG", "UDHAM SINGH N", "BAGESHWAR"), (
                "AMBALA", "GURGAON", "HISAR", "JIND", "KARNAL", "MAHENDRAGARH", "ROHTAK", "BHIWANI", "FARIDABAD",
                "KURUKSHETRA", "SIRSA", "SONEPAT(RTK)", "YAMUNANAGAR", "KAITHAL", "PANIPAT", "REWARI", "FATEHABAD",
                "JHAJJAR", "PANCHKULA", "MEWAT", "PALWAL(FRD)"), ("CHANDIGARH"), (
                "NEW DELHI", "CENTRAL DELHI", "EAST DELHI", "NORTH DELHI", "NE DELHI", "SW DELHI", "NW DELHI",
                "SOUTH DELHI", "WEST DELHI"), (
                "AMRITSAR", "BATHINDA", "FEROZEPUR", "GURDASPUR", "HOSHIARPUR", "JALANDHAR", "KAPURTHALA", "LUDHIANA",
                "PATIALA", "RUPNAGAR", "SANGRUR", "FARIDKOT", "MOGA", "NAWANSHAHR", "FATEHGARH SAH", "MUKTSAR", "MANSA",
                "BARNALA", "SAS NAGAR(MGA)", "TARN TARAN"), (
                "BILASPUR", "CHAMBA", "KANGRA", "KINNAUR", "KULLU", "LAHUL & SPITI", "MANDI", "HAMIRPUR", "SHIMLA",
                "SIRMAUR", "SOLAN", "UNA"), (
                "ANANTNAG", "BARAMULLA", "DODA", "JAMMU", "KATHUA", "LADAKH (LEH)", "UDHAMPUR", "BADGAM", "KUPWARA",
                "PULWAMA", "SRINAGAR", "KARGIL", "POONCH", "RAJOURI", "BANDIPORE", "GANDERWAL", "KULGAM/(ANT)",
                "SHOPAN", "SAMBA", "KISTWAR", "REASI", "RAMBAN(DDA)"), (
                "BARMER", "BIKANER", "CHURU", "SRI GANGANAGA", "JAISALMER", "JALORE", "JODHPUR", "NAGAUR", "PALI",
                "HANUMANGARH", "AJMER", "ALWAR", "BANSWARA", "BHARATPUR", "BHILWARA", "BUNDI", "CHITTORGARH",
                "DUNGARPUR", "JAIPUR", "JHALAWAR", "JHUNJHUNU", "KOTA", "SAWAI MADHOPUR", "SIKAR", "SIROHI", "TONK",
                "UDAIPUR", "DHOLPUR", "BARAN", "DAUSA", "RAJSAMAND", "KARAULI", "PRATAPGARH(CHT"), (
                "BETUL", "VIDISHA", "BHIND", "DATIA", "DEWAS", "DHAR", "GUNA", "GWALIOR", "HOSHANGABAD", "INDORE",
                "JHABUA", "MANDSAUR", "MORENA", "KHANDWA", "KHARGONE", "RAISEN", "RAJGARH", "RATLAM", "SEHORE",
                "SHAJAPUR", "SHIVPURI", "UJJAIN", "BHOPAL", "HARDA", "NEEMUCH", "SHEOPUR", "BARWANI", "ASHOKNAGAR(GNA",
                "BURHANPUR", "ALIRAJPUR(JBA)", "BALAGHAT", "CHHATARPUR", "CHHINDWARA", "JABALPUR", "MANDLA",
                "NARSINGHPUR", "PANNA", "REWA", "SAGAR", "SATNA", "SEONI", "SHAHDOL", "SIDHI", "TIKAMGARH", "KATNI",
                "DINDORI", "UMARIA", "DAMOH", "ANUPPUR(SHAHD", "SINGRAULI"), (
                "AHMEDABAD", "BANASKANTHA", "BARODA", "BHARUCH", "VALSAD", "DANGS", "KHEDA", "MEHSANA", "PANCHMAHALS",
                "SABARKANTHA", "SURAT", "GANDHINAGAR", "NARMADA(BRC)", "NAVSARI(VSD)", "ANAND(KHR)", "PATAN(MHSN)",
                "DAHOD(PNML)", "TAPI(SRT)", "AMRELI", "BHAVNAGAR", "JAMNAGAR", "JUNAGADH", "KUTCH", "RAJKOT",
                "SURENDRANAGAR", "PORBANDAR"), ("DNH"), ("DAMAN", "DIU"), (
                "MUMBAI CITY", "RAIGAD", "RATNAGIRI", "THANE", "SINDHUDURG", "MUMBAI SUB", "AHMEDNAGAR", "DHULE",
                "JALGAON", "KOLHAPUR", "NASHIK", "PUNE", "SANGLI", "SATARA", "SOLAPUR", "NANDURBAR", "AURANGABAD",
                "BEED", "NANDED", "OSMANABAD", "PARBHANI", "LATUR", "JALNA", "HINGOLI", "AKOLA", "AMRAVATI", "BHANDARA",
                "BULDHANA", "CHANDRAPUR", "NAGPUR", "YAVATMAL", "WARDHA", "GADCHIROLI", "WASHIM", "GONDIA"),
                ("NORTH GOA", "SOUTH GOA"), (
                "BASTAR", "BILASPUR", "DURG", "RAIGARH", "RAIPUR", "SURGUJA", "RAJNANDGAON", "DANTEWADA",
                "KANKER (NORH", "JANJGIR-CHAMP", "KORBA", "JASHPUR", "DHAMTARI", "MAHASAMUND", "KORIYA",
                "KOWARDHA (KAB", "NARAYANPUR", "BIJAPUR"), (
                "EAST GODAVARI", "WEST GODAVARI", "GUNTUR", "KRISHNA", "NELLORE", "PRAKASAM", "SRIKAKULAM",
                "VISAKHAPATNAM", "VIZIANAGARAM", "ADILABAD", "HYDERABAD", "KARIMNAGAR", "KHAMMAM", "MAHABUBNAGAR",
                "MEDAK", "NALGONDA", "NIZAMABAD", "WARANGAL", "RANGAREDDY", "ANANTAPUR", "CHITTOOR", "KUDDAPAH",
                "KURNOOL"), (
                "VELLORE", "COIMBATORE", "DHARMAPURI", "KANYAKUMARI", "CHENNAI", "MADURAI", "NILGIRIS", "RAMANATHAPURA",
                "SALEM", "THANJAVUR", "TIRUCHIRAPPAL", "TIRUNELVELI", "ERODE", "PUDUKKOTTAI", "DINDIGUL",
                "VIRUDHUNAGAR", "SIVAGANGA", "THOOTHUKUDI", "TIRUVANNAMALA", "NAGAPATTINAM", "VILUPPURAM", "CUDDALORE",
                "KANCHIPURAM", "TIRUVALLUR", "THENI", "NAMAKKAL", "KARUR", "PERAMBALUR", "TIRUVARUR", "KRISHNAGIRI",
                "ARIYALUR", "TIRUPUR"), ("PONDICHERRY", "KARAIKAL", "MAHE", "YANAM"), (
                "UTTAR KANNADA", "DAKSHIN KANDA", "UDUPI", "BELGAM", "BIDAR", "BIJAPUR", "DHARWAD", "GULBARGA",
                "YADGIR", "RAICHUR", "BAGALKOTE", "GADAG", "HAVERI", "KOPPAL", "BANGALORE RUR", "BELLARY",
                "CHIKMAGALUR", "CHITRADURGA", "KODAGU", "HASSAN", "KOLAR", "MANDYA", "MYSORE", "SHIMOGA", "TUMKUR",
                "BANGALORE URB", "CHAMARAJANAGA", "DAVANGERE", "RAMNAGAR(BNGR)", "CHICKBALLAPUR"), (
                "ALAPPUZHA", "CANNUR", "ERNAKULAM", "KOTTAYAM", "KOZHIKODE", "MALAPPURAM", "PALAKKAD", "KOLLAM",
                "THRISSUR", "THIRUVANANTHA", "IDUKKI", "KASARGOD", "PATHANAMTHITTA", "WAYANAD"), ("LAKSHADWEEP")]
State = ["ANDAMAN And NICOBAR ISLANDS", "ARUNACHAL PRADESH", "ASSAM", "MEGHALAYA", "MANIPUR", "MIZORAM", "NAGALAND",
             "TRIPURA", "WEST BENGAL", "SIKKIM", "ORISSA", "JHARKHAND", "BIHAR", "UTTAR PRADESH", "UTTARANCHAL",
             "HARYANA", "CHANDIGARH", "DELHI", "PUNJAB", "HIMACHAL", "JAMMU AND KASHMIR", "RAJASTHAN", "MADHYA PRADESH",
             "GUJARAT", "DADAR NAGAR HAVELI", "DAMAN AND DUI", "MAHARASHTRA", "GOA", "CHATISGARH", "ANDHRA PRADESH",
             "TAMIL NADU", "PONDICHERRY", "KARNATAKA", "KERALA", "LAKSHADWEEP"]
with st.sidebar:
    selected = option_menu('ML 03',

                           ['Crop Prediction',
                            'Fertilizer Prediction',
                            'Suggesting Crops'],
                           icons=['house', 'gear', 'person'],
                           default_index=0)
if (selected == 'Crop Prediction'):

    add_bg_from_local('i.jfif')
    st.markdown("<h1 style='text-align: center; color: black;'>CROP PREDICTION</h1>", unsafe_allow_html=True)
    filename = "crops.sav"

    loaded_model = pickle.load(open(filename, "rb"))
    st.markdown("<hr style=color: black;'></hr>", unsafe_allow_html=True)
    st.markdown(
        "<h5 style='text-align: center; color: purple;'>--------------------------- Soil Composition -------------------------------</h5>",
        unsafe_allow_html=True)

    N = float(st.number_input("Nitrogen Value: "))
    P = float(st.number_input("Phosphorus Valu: "))
    K = float(st.number_input("Potassium Value: "))
    ph = float(st.number_input("PH value : "))
    soil = st.selectbox("Select Soil", ('Sandy', 'Loamy', 'Black', 'Red', 'Clayey'))
    st.markdown("<hr style=color: black;'></hr>", unsafe_allow_html=True)
    st.markdown(
        "<h5 style='text-align: center; color: purple;'>--------------------------------- Location ----------------------------------</h5>",
        unsafe_allow_html=True)
    state = st.selectbox("Select Your State", (
    "ANDAMAN And NICOBAR ISLANDS", "ARUNACHAL PRADESH", "ASSAM", "MEGHALAYA", "MANIPUR", "MIZORAM", "NAGALAND",
    "TRIPURA", "WEST BENGAL", "SIKKIM", "ORISSA", "JHARKHAND", "BIHAR", "UTTAR PRADESH", "UTTARANCHAL", "HARYANA",
    "CHANDIGARH", "DELHI", "PUNJAB", "HIMACHAL", "JAMMU AND KASHMIR", "RAJASTHAN", "MADHYA PRADESH", "GUJARAT",
    "DADAR NAGAR HAVELI", "DAMAN AND DUI", "MAHARASHTRA", "GOA", "CHATISGARH", "ANDHRA PRADESH", "TAMIL NADU",
    "PONDICHERRY", "KARNATAKA", "KERALA", "LAKSHADWEEP"))
    i = State.index(state)
    district = st.selectbox("Select Your District", District[i])

    response_API = requests.get(
        'https://api.mapbox.com/geocoding/v5/mapbox.places/' + district + ' ' + state + '.json?access_token=pk.eyJ1Ijoic2FpZ29ydGk4MSIsImEiOiJja3ZqY2M5cmYydXd2MnZwZ2VoZzl1ejNkIn0.CupGYvpb_LNtDgp7b-rZJg')
    data = response_API.text
    parse_json = json.loads(data)
    coordinates = parse_json['features'][0]['center']
    y = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=' + str(coordinates[1]) + '&lon=' + str(
        coordinates[0]) + '&appid=8d51fbf3b5ad7f3cc65ba0ea07220782')
    data1 = response_API.text
    parse_json1 = json.loads(data)

    humidity = y.json()['main']['humidity']
    temperature = (y.json()['main']['temp'] - 273)
    df2 = pd.read_csv("data2.csv")
    st.markdown(f"<h6 style='text-align: center; color: black;'>The Temperature of this location is {temperature}</h6>", unsafe_allow_html=True)
    st.markdown(f"<h6 style='text-align: center; color: black;'>The Humidity of this location is {humidity}</h6>",unsafe_allow_html=True)

    crop = ['rice', 'maize', 'chickpea', 'kidneybeans', 'pigeonpeas',
            'mothbeans', 'mungbean', 'blackgram', 'lentil', 'pomegranate',
            'banana', 'mango', 'grapes', 'watermelon', 'muskmelon', 'apple',
            'orange', 'papaya', 'coconut', 'cotton', 'jute', 'coffee']
    index = [20, 11, 3, 9, 18, 13, 14, 2, 10, 19, 1, 12, 7, 21, 15, 0, 16,
             17, 4, 6, 8, 5]
    res = {}
    for key in index:
        for value in crop:
            res[key] = value
            crop.remove(value)
            break


    def prediction(input_data):
        input_data_as_numpy_array = np.asarray(input_data)
        input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
        prediction = loaded_model.predict(input_data_reshaped)
        return res[prediction[0]]


    q = df2[(df2.STATE_UT_NAME == state) & (df2.DISTRICT == district)]
    total = 0
    month = ['January', 'Feburary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
             'November', 'December']
    month_index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    res1 = {}
    for key in month:
        for value in month_index:
            res1[key] = value
            month_index.remove(value)
            break
    st.markdown("<hr style=color: black;'></hr>", unsafe_allow_html=True)
    st.markdown(
        "<h5 style='text-align: center; color: purple;'>--------------------------------- Season ----------------------------------</h5>",
        unsafe_allow_html=True)
    a = st.selectbox("Starting month of cultivation", (
    'January', 'Feburary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
    'December'))
    b = st.selectbox("Ending month of cultivation", (
    'January', 'Feburary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
    'December'))

    start_month = int(res1[a])
    end_month = int(res1[b])

    if start_month <= end_month:
        l = (end_month - start_month) + 1

        for i in range(start_month, end_month + 1):
            try:
                total += int(q[i:i + 1].value)
            except:
                total -= 1

    elif start_month > end_month:
        l = (end_month + 12) - start_month + 1

        for i in range(start_month, 13):
            try:
                total += int(q[i:i + 1].value)
            except:
                total -= 1

        for i in range(1, end_month + 1):
            try:
                total += int(q[i:i + 1].value)
            except:
                total -= 1

    avg_rainfall = total / l
    st.markdown(f"<h6 style='text-align: center; color: black;'>The Average Rainfall is {avg_rainfall}</h6>",unsafe_allow_html=True)

    st.markdown("<hr style=color: black;'></hr>", unsafe_allow_html=True)

    if st.button("Predict"):
        st.markdown(
            f"<br/><h5 style='background-color:green; padding: 5px 20px 5px 5px;text-align: center;color: black;'>  Recommended Crop:  {prediction([N, P, K, temperature, humidity, avg_rainfall, ph])}</h5>",
            unsafe_allow_html=True)
        
if (selected == 'Fertilizer Prediction'):
    st.title("Fertilizer Prediction")
    st.markdown("<hr style=color: black;'></hr>", unsafe_allow_html=True)
    filename = "crops_fertilizer.sav"
    add_bg_from_local('img2.jfif')

    loaded_model1 = pickle.load(open(filename, "rb"))
    state = st.selectbox("Select Your State", (
        "ANDAMAN And NICOBAR ISLANDS", "ARUNACHAL PRADESH", "ASSAM", "MEGHALAYA", "MANIPUR", "MIZORAM", "NAGALAND",
        "TRIPURA", "WEST BENGAL", "SIKKIM", "ORISSA", "JHARKHAND", "BIHAR", "UTTAR PRADESH", "UTTARANCHAL", "HARYANA",
        "CHANDIGARH", "DELHI", "PUNJAB", "HIMACHAL", "JAMMU AND KASHMIR", "RAJASTHAN", "MADHYA PRADESH", "GUJARAT",
        "DADAR NAGAR HAVELI", "DAMAN AND DUI", "MAHARASHTRA", "GOA", "CHATISGARH", "ANDHRA PRADESH", "TAMIL NADU",
        "PONDICHERRY", "KARNATAKA", "KERALA", "LAKSHADWEEP"))
    i = State.index(state)
    district = st.selectbox("Select Your District", District[i])

    response_API = requests.get(
        'https://api.mapbox.com/geocoding/v5/mapbox.places/' + district + ' ' + state + '.json?access_token=pk.eyJ1Ijoic2FpZ29ydGk4MSIsImEiOiJja3ZqY2M5cmYydXd2MnZwZ2VoZzl1ejNkIn0.CupGYvpb_LNtDgp7b-rZJg')
    data = response_API.text
    parse_json = json.loads(data)
    coordinates = parse_json['features'][0]['center']
    y = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=' + str(coordinates[1]) + '&lon=' + str(
        coordinates[0]) + '&appid=8d51fbf3b5ad7f3cc65ba0ea07220782')
    data1 = response_API.text
    parse_json1 = json.loads(data)

    humidity = y.json()['main']['humidity']
    temperature = (y.json()['main']['temp'] - 273)
    df2 = pd.read_csv("data2.csv")
    st.markdown(f"<h6 style='text-align: center; color: black;'>The Temperature of this location is {temperature}</h6>",unsafe_allow_html=True)
    st.markdown(f"<h6 style='text-align: center; color: black;'>The Humidity of this location  is {humidity}</h6>",unsafe_allow_html=True)

    st.markdown("<hr style=color: black;'></hr>", unsafe_allow_html=True)
    crop = ['Maize', 'Sugarcane', 'Cotton', 'Tobacco', 'Paddy', 'Barley',
       'Wheat', 'Millets', 'Oil seeds', 'Pulses', 'Ground Nuts']
    index = [ 3,  8,  1,  9,  6,  0, 10,  4,  5,  7,  2]
    res = {}
    for key in crop:
        for value in index:
            res[key] = value
            index.remove(value)
            break
    res3={}
    pre1=['Urea', 'DAP', '14-35-14', '28-28', '17-17-17', '20-20',
       '10-26-26']
    pre2=[6, 5, 1, 4, 2, 3, 0]
    for key in pre2:
        for value in pre1:
            res3[key] = value
            pre1.remove(value)
            break

    def prediction(input_data):
        input_data_as_numpy_array = np.asarray(input_data)
        input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
        prediction = loaded_model1.predict(input_data_reshaped)
        return res3[prediction[0]]
    N = float(st.number_input("Nitrogen Value: "))
    P = float(st.number_input("Phosphorus Value: "))
    K = float(st.number_input("Potassium Value: "))
    ph = float(st.number_input("PH value : "))
    moisture = float(st.number_input("Moisture value : "))
    cr=st.selectbox("Select crop",('Maize', 'Sugarcane', 'Cotton', 'Tobacco', 'Paddy', 'Barley',
       'Wheat', 'Millets', 'Oil seeds', 'Pulses', 'Ground Nuts'))
    crop=int(res[cr])
    x=['Sandy', 'Loamy', 'Black', 'Red', 'Clayey']
    y=[4, 2, 0, 3, 1]
    res2 = {}
    for key in x:
        for value in y:
            res2[key] = value
            y.remove(value)
            break
    so=st.selectbox("Select Soil",('Sandy', 'Loamy', 'Black', 'Red', 'Clayey'))
    soil=int(res2[so])
    st.markdown("<hr style=color: black;'></hr>", unsafe_allow_html=True)
    if st.button("Predict"):
        '''st.markdown(
            f"<br/><h5 style='background-color:green; padding: 5px 5px 5px 5px;text-align: center;color: black;'>  Recommended Fertilizer:  {prediction([temperature,humidity,moisture,soil,crop,N,P,K])}</h5>",
            unsafe_allow_html=True)'''
        st.success(f"Recommended Fertilizer:  {prediction([temperature,humidity,moisture,soil,crop,N,P,K])}")


if (selected == 'Suggesting Crops'):
    df = pd.read_csv("Crops.csv")

    st.title("Suggestion of crops")
    from PIL import Image

    image = Image.open('img.jfif')

    st.image(image, width=700)
    st.markdown("<hr style=color: black;'></hr>", unsafe_allow_html=True)
    state = st.selectbox("Select Your State",
                         ('select State', 'Andaman and Nicobar', 'Andhra Pradesh', 'Assam', 'Chattisgarh',
                          'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh',
                          'Jammu and Kashmir', 'Karnataka', 'Kerala', 'Madhya Pradesh',
                          'Maharashtra', 'Manipur', 'Meghalaya', 'Nagaland', 'Odisha',
                          'Pondicherry', 'Punjab', 'Rajasthan', 'Tamil Nadu', 'Telangana',
                          'Tripura', 'Uttar Pradesh', 'Uttrakhand', 'West Bengal'))
    District = df[df.state == state]['district']
    district = st.selectbox("Select Your District", tuple(District.unique()))
    Market = df[df.district == district]['market']
    market = st.selectbox("Select the Market", tuple(Market.unique()))

    x = df[(df.state == state) & (df.district == district) & (df.market == market)]
    y = x.sort_values(by=['modal_price'], ascending=False)
    z = y['commodity'].tolist()
    if st.button("Suggest"):
        for i in range(len(z)):
            print(z[i])
            st.success(z[i])
