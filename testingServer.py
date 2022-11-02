import pytest
import requests
import configparser

# passing the api endpoint of the lambda function
awsLink = "https://49jyovhul2.execute-api.us-east-2.amazonaws.com/Prod/hello"

configServer = configparser.ConfigParser()
configServer.read("configFileServer.ini")
configData = configServer['Server']

#testing if the input parameters are not none
def testNoneCheck():
    assert (configData['awsendpointapi'] is not None and configData['maxworkers'] is not None and configData['portnumber'] is not None)
# testing the input parameters to the configuration file parameters
def testConfig():
    assert (configData['awsendpointapi'] == awsLink and configData['maxworkers'] == "10" and configData['portnumber'] == "50051")

# sending an input that is not present in the s3 bucket.
def test1():
    date = "2022-11-23"
    time = "10:00:00.000"
    deltaTime = "10"
    pattern = "INFO"
    params = {'date': date, 'time': time, 'deltaTime': deltaTime, 'pattern': pattern}
    response = requests.get(awsLink, params=params)
    assert (response.text == "False. No file under the requested date")

# the input time is not within the given file
def test2():
    date = "2022-10-23"
    time = "10:00:00.000"
    deltaTime = "10"
    pattern = "INFO"
    params = {'date': date, 'time': time, 'deltaTime': deltaTime, 'pattern': pattern}
    response = requests.get(awsLink, params=params)
    assert (response.text == "False. Given input time is not present in the log file for the  date you provided")

# The test is for sending an input which crosses the timelimit given in the file hence it returns only the hash value for the given time limit
def test3():
    date = "2022-10-23"
    time = "21:35:00.000"
    deltaTime = "20"
    pattern = "ERROR"
    params = {'date': date, 'time': time, 'deltaTime': deltaTime, 'pattern': pattern}
    response = requests.get(awsLink, params=params)
    assert (response.text == '9fc42b3bdd0f4b688537e7872cde50ec, 3ed7d4c42124d2545a33f156f1fb793f,  are the md5 hash values generated for time interval 21:31:53.005000 to 21:41:21.669000')

# The test is to find the working of the algorithm when there is no pattern given
def test4():
    date = "2022-10-23"
    time = "21:35:00.000"
    deltaTime = "20"
    pattern = "INFOTAINMENT"
    params = {'date': date, 'time': time, 'deltaTime': deltaTime, 'pattern': pattern}
    response = requests.get(awsLink, params=params)
    assert (response.text == "False. No such pattern exists for the given time interval 21:31:53.005000 to 21:41:21.669000")

#This test performs with every right parameter given as input and expecting a proper response from the lambda fucntion
def test5():
    date = "2022-10-24"
    time = "20:40:00.000"
    deltaTime = "10"
    pattern = "INFO"
    params = {'date': date, 'time': time, 'deltaTime': deltaTime, 'pattern': pattern}
    response = requests.get(awsLink, params=params)
    assert (response.text == 'd266272b79ccd9bc9bf1058b912ec2a9, d95b305648f1412f9e0ea8e5e6e30868, '
 'e3fc7bf406aff9e85ee5ebf13ef88e4f, b60a593b03d0258cfa9ea5898d27123d, '
 '44bd0ec8b83bf27e8933d36509f15a2c, 111ea4e256190e542881d05624d3ae6d, '
 '4154b214a1618beb07e732395515f4f4, 10cc514fdefed21a33fd908e476147e5, '
 '44f71049cf09d33901cd4b42cf2bc62a, 6e27a4f6c89d2c05afaadf338f8e03b4, '
 '2b4c435cc1795e56eae3a204443d20bf, 63fd06edb824ca0221e18725101a0f48, '
 '372b81bb51d55d6f216c9885cda88503, 83afb27e824e91219e879c320ed69b25, '
 'b30489e8e483cbc13b01619d1c10c8ae, 15f51e746cedee97dc08d09af78aa69e, '
 '93fbb8605eb3cc75e831746e210cf140, f65b3189f20545995808ddffc6cae51f, '
 '1605028a7e10068504904709bb27d167, 1091a53f67940df437dac669aa55fdb4, '
 'f4385afab4cb12ef2dd2e9c397b38feb, 7f402beab5c12dc9b809e30d7593165f, '
 '8452cd6d765686ca73114a05997a415d, 445f333596d4481832a0afd0646803da, '
 '1ebcdbc9378eba5ac2d9e9442b2a6b78, 17f05324e7f6d17c0ba8eaef0d5843a8, '
 'ed57463e8b5d9abfeec248e872c76907, ff5808298b42a4500ad2a786ddf13fe4, '
 '8971e6098848e0dbe1a7999e76634ecc, 9892f3fc655b789527dc783e57f4657e, '
 '94cf5f0a0e22e491682fe1160291091f, 5670007eaf263d75d4efcffdabab4042, '
 'c39fa2ef752a4c8f0a230833ae1dbfff, da8976c337c7d136ebea26ef5996d8fa, '
 'b6d4f13024dff62c4def34ea9ba9498e, 67216591e3d9d2a4adf6173bb1710c6a, '
 'f995688952f7ae9a998412074295a7a9, 3a31fe7cdf00fe25c981a1be70fd138f, '
 '8bfe4bc726e116c44ca45559c66330ba, 2afbea963951059eefa425673897601f, '
 '853574c737f8dafeae2e98c767ae2146, e9eb0d0a197e8b2ca47b727fbf5c2223, '
 '1993ee32802889450cb2477997c21eca, 2494fe486193b70e51bdb08190a0cf4c, '
 'e37ca3ce8978129f0064a6710e8b279b, b2aa7471c7cec21d098f2fd22352aea5, '
 'dcff2273476fb5d8e30bac3d8f2de811, 6da491014db0ec4243a95e267346542c, '
 'a152bd99f3d9af70b821e3dd33bda7fd, 065608bbc9eb927dc91fedcb25ff284a, '
 '76c97b59f82c49767b8488e9a47878cb, 18003959cea257c29b7b66fd12b4bcd5, '
 'c7ac3df17401c5f664777a06056dc156, dc5acf31b3d1326eedf9a71926baa671, '
 'c3860688443d081844b3ab7d87e05d2b, 115453d9b2174ef672fd48b77e43389b, '
 'd8ca54c7f7688c0b79399814ccad10b7, 53cdc7d9bab3046f2cd18f97a76c65da, '
 '71295708bb8dd007a17cf26c2ec5f8d0, a0a4c749c99794de3c426e41328b4a7a, '
 'c829709c8f4980df899a5a867eca3293, ccbb1e95b0b4ec41074b93fc47e85b0a, '
 'd514529e95915d5bb4d7bd532e569de1, ff7dc65e008f47f561f884aa1f2954be, '
 '840a297f788c5288413637eb05a13f2c, ffbaeeb4fef817dc69313a0a4c38aa31, '
 '4aacdb65b49005cf4e527395bdc30776, 85cbef822be742769f80786b02a6563f, '
 '87e198672c3fd156fafeeec67ac300c9, 087a22831039b41738b49e38ffa1c990, '
 'dae0e393994ddce7d63840e0654d520b, 893ff3a387b548ccb548d673f106e7f4, '
 'f7b7d7af16cd4163ba4a84d53005d983, 8dd760adf463c1b7f788cf516a4e3346, '
 'e28ae8e9ffc3455eb0bc42a0c1aab8e8, 40817558eade4cfbe6c0bd9b62ecdb2f, '
 'e13ff3944fbebc11a708d29567c6e35b, cc7bfbc4d1eb9f650153c9758f2d7615, '
 '3649d03c614f816345740435a1938356, 0891a236ee580b92c792ffba6dff8b66, '
 '99b8f227b5a41fb5d8aeddc85779e39c, 30d95467944f31c80b973e47cc78fdac, '
 '631e4563059ce869894c8a1c59c53bee, 38d91a7306c9e6d875fbffe3102c0d70, '
 'e8e2effa85cdf07624f1f8d312ba11e5, 1a2729d1f165f7e71d1c20eb269355f1, '
 'e401675b68656ca9be32d4a5df4b90e6, 9bf4297a9e7d4c142fc9086c4b50b130, '
 '72466a7c48578061a85d7443ed26a0ed, 8330a29cb34a7b7a58f187938b5f2183, '
 'c653309908aae4bf72d2d112155bcf2c, 575f6041f4824d4cffa29ddd49fecfa9, '
 'b4be798b6b4491e723433ed8dc21a2a2, c8ce6c881959a10b40bd510a4e41b1ae, '
 'b09cd468e97ab5c1d50821ac78dec927, 451b7c1b77a0dad7e84745eaef8d7a34, '
 '2aa88d148dbd26fe6b0a9b4e2ae8c4a1, 9011c948f64785da4e99ebe20bdaeb70, '
 '302c47766a15583cfff1eb59eba4bc4f, 6506e689352bb3629784965981e2dbf4, '
 '182c3c38b0ae3a2739f5cbd6f539d7e8, 6dd33e6d31c554d3840c4f0d558b4d2b, '
 'b2b5f1476b9b7f11929e2e47ecfc86e2, af1d191c183da0d7a1566cba782883d6, '
 '0d9b10cbcc104f4974655790ee7d2174, 008dc54c05bfd33e19bb6c8ddfffa6f5, '
 'e80c7e4dd3767fa716c630f2d5b32d86, 048c5f687ab41ecd2ccd57339d9d08ec, '
 'b48da4281f0598ecbccc33e6b837e472, 40bf7a8dd3d3520bb6928356dc05b61a, '
 '2c4c5b0f97637b868cc16cc6a08fbeaa, 72f834f2f7e86e7b24e4b39636d80639, '
 'e7e8c71dd3bd399aa3ea0e895c91d24d, d4186489e60669eef721283adc46d9a3, '
 '802a5f09c28d70c0c9318e4ff74f46f5, 6564d0f30623c275435fd68aeda88e28, '
 '38112081e512bba712936bba16bbc91d, 4ae5c617d8a5750cd669efe1dab397f4, '
 '307e1a6119c237a25fcca6f8c61fc900, ae79e0e469822ca43c9037cec1d83187, '
 'd0d5b499d2beecb7bf649adb11b42dd8, 9dee975cadeeb9ca95ab6b036a5f47b2, '
 'b2ee30f78a328f741ef1e151c29c01ab, e19441c8f15778d95de9c0606c6cedfb, '
 '2a11a836301760f002ac8dbde9eee12f, 37b25baa2253a31428b20ba225f01a30, '
 'cc7e7967e584aca4c7867f58e4889fe7, 663366c0f0877d192d499a4fc9778b89, '
 '4831f31cb71619069ddecd5a4e16ef44, fd98dfd8947c700a0cb4c3951caf989b, '
 '2ce96b661cb5dbaa4cb8229372bd9059, 63f47c61f7bb35b48e3078860cb2b312, '
 'e8ec4c5af1e522101cf7a6f8f52077d0, bceda4ce95678f2dc60304fef6010898, '
 'd7259cc8bc4fb87484d8ac44325aee23, bf0c18faae6922d8a96f16e2eb08ff42, '
 '94802af4d4195cd1b7da6d1a579d620f, 3abb2ca1cc92e346355564a7998bd917, '
 '524ecb5c6400604d9a3013b7ea9f93c3, fa6a553a6166b6f42f60ea7c95f11968, '
 'f3632f4c034b19ac8a12824b8650cea0, 736c56de30ff6261bccdede668c3e6c1, '
 '47cdebecfbfd5c3c591e01ce159b612b, 33a4848cdf86a2a4dd6f2bef9e17008b, '
 '7b441140f82327b493bc686a1555d7dc, 5be01a02f85db31560f14a92bf6bb0ce, '
 'b319bf1bd19fe4c9a7455b8cd12c3894, 75ba9eef8dbc2698f40b99f31ade3834, '
 '9fd24316c713a28344b0989ea3dc01a5, 862b26d4d478fc4cefb0cd9f709efbd5, '
 'faf69be067a4d19b992752203f8d9f4d, afc92b3bdd41c5593623858e60af7977, '
 'e5e4ba9f8b9fab246cd06df6555e4654, 6739e8c13f30295cf12ae753965c7a06, '
 '6db1979a6f2fe505f699748608bd5e5e, 355ed79585b0c929b38df39109ecd430, '
 '24350053a835abca8b7950944ad09c18, 812688b370d24ced6b1c7c78c7fc9139, '
 '29bd0f5be3b320490182fd617ebd3d52, 25098554b11454539e896cb74d72e8b4, '
 '230453c190694bb300d3517335b428b3, 495347fb9ad1e1e81c83649322058b6c, '
 '2658a907d012b75c37373dcb659b3cb0, 0741e808fd47ed753cd78e915de76a20, '
 'b78c064ee34e8b1c05d227e17b31cc35, c1fa5328249991e23c1cc566fa5697ef, '
 '1a2708e1a07cc80b5a1db2aa4f21a921, ee6655031fc523e0c554259cd8f4a8f6, '
 'e55e4a9706fa79e700e6fc8ba1090f42, 40245131bbfe81b1d6fcacd08bedc84f, '
 '15cafe992ddab7657c7a4adb6e03e500, e6b957c3e479009bb7f03b2e61eb6ce4, '
 '6a8a9adba59130e08590d6523258b46a, c110b3353b0d475bc99f2471baad5989, '
 'c27a2d921ac2f8b764e8fc2e063b5bc0, 023517c9529ce8b18659634be84637b7, '
 '38de8ba474836fb9e37d8a5481f6b8fc, 450f66e87055b43658afcc146c3d2db2, '
 '8be888b5016afd28b18d5b93266c4a36, 8755dcd567b5861d2d5db20dff08cede, '
 'b3d3b4ab8ef1a4b0c6280930413cb713, 67b49b4f8284a1b18b554f3379e89d8d, '
 'fca5c12fb382379be2e000c0e8d6ffbf, 22bcd59907914bfaafa8b424f7d70e4c, '
 '49363202320de1eb81e52a05e714e133, 1ca2bcf46374e7317f3f970461345820, '
 '3f888806a5a4972a0e2ad82b1cf53b6d, a4606e6b8b5d8b3f2036cd827ac42e23, '
 '7e9f398e9eb95a212ee52c5753230df6, 44af052382e4e2cee7bab8ed303c2bdc, '
 '9f87547845c5c1b9693190042d8a0017, 4ec9a97874d00091750ebed54d360bd7, '
 '984237b0c50820076aa01529ebbf7841, e01f8456ceb2bce4393fee2a604f9da1, '
 '9bf113cf1728eaab62d5bd23963000b0, bdcbac8a09f3ce4b44a8ad76350c4bd5, '
 'fe315764142b0cd01c1b720f9201377b, 66a5f2a3a181ff452eb08ff31560dc15, '
 '80019bde32a803ec34fb5c372c9993bc, 92e3a2a5b2f1ff0ae1868c426f7586b2, '
 '37679f4b3a39f2160827eab27ddb5f7b, 79916b7c11bfb8fba4308ac759d91841, '
 '65c804ae4660f0faf19cb8fa2ac8201e, c1137e0f897e001b320f3a91c8b25245, '
 '0b80532f87d881365cb77b9c43324406, 872946e332eb5e287f369d40632700e5, '
 'fda08a1e83877872db76c54e5b0101b4, 5509683275826185427ad9cbc1563d8c, '
 '91d7f49f518f584666fa32463ce429d0, 384ad62326ca019568ab3859a9dfca32, '
 'c83dd77a2cdfb598974b1264da5b75f8, 702d47a3e5d930f8842898f632a2ead3, '
 '9ba95efb6a81be60eee5da1df59c90d2, 3596593543b6e0de0c2d91ebfcebb598, '
 '9f79598de0f87eff4d3f1c691a7361e3, 8e891354f51589f5101028a7f8a99808, '
 'a1e77692d6a9984c3c92b8203717a647, 3974f58ff0c5f4ce834fc4da5d9d15f4, '
 '0b467bb3ce746daa8301e3512140744c, 37d242c40448f89f9df4e9adb8f42385, '
 '9e99548eaa404da7e6371a1a7fde89b0, cfb1691e4e74fa4d29840fd5aabd948d, '
 'ac02dd11daef87610d3760a3eecfa9a8, ceb8feda6344b716176033c4829a3408, '
 '42fd39290d0ef14049890ff383eaa74b, 95ff4b755b896efd54f17fdc44feee9e, '
 '5189800c4299361cb3833dd7a78a3db5, 1e400f9a604cb20e697a31910ef79d6d, '
 '6b34a3cbdb887484119c367022bac70b, 35f6b1397b7fdff85ab2e548429c3487, '
 'd38af071ec88ef057144ca223c510908, a36da2003380f21e016ece92f333fbc0, '
 'e3aa5e5afc95c66e0972b8b6b6a40f76, 3587f02cfb4449736a21a5a14afe2b84, '
 'ebc0721be339653036b5641a75688a5e, f594fce30d35f4285aba8d243247ef07, '
 'a0a830ea7398ab393fec6b66699eb29d, 8b761f4919ed054ba483e0ddae33fa23, '
 '2f3617441b4594a0b07688f3f6c114f0, a93a528c12bb3c9cc46ad161b8ad2287, '
 'baa65ebf527da9afff756238599e1813, b8314e65a46d9496fd99f5247673c7de, '
 '51ecc77a32fb641e8e16a76cba2e23d8, 2194a1cb12f44b194d523b987d6e4a46, '
 'b70779a3acc266c4860ac2a9449a91f3, b8df29a5276a8e296305a28666673361, '
 '3f29aa2cb3bcbd238d57d77cb7dd6d95, bd6f58ead1ffd8e613d1897b45009959, '
 '490c7c52f1385ab98dfb485eda365675, a1da15fb4a08939d0c3f8a39e18837c6, '
 'ef22f8d1cdc42679d2ff5eeccda290b6, f15cb0eb2bbeb065a031a19239ca70e4, '
 '7b039a23f7b3179cab3a32258d248a35, b186bea18c38641463c9b63e0b507176, '
 'ecb6d35959a4b15944a517be31b264b3, 49cb65d42597215a915a3e4413aec3e3, '
 '693c294fec47e511abd7f924f85738a1, 336823199462d608c1d964347416c19a, '
 'b2064b7b44af28711a8f56aed3de439c, 7cf4f67ffe18834421f26dbd91adc508, '
 '45d70fa927e8ce4f811e4ff2a6a1cb47, 458506fd7fa60ff08fb0cd7f07af7e51, '
 '8cc847a6436fdf5da8f33181fcecb0f8, 0fb226c5d4bc3e31332b3a4b02d22388, '
 '3e21a3ca11fa0817c2b5fd38b47ac91e, 369a2f14f7abb2b7d361a72953f6453e, '
 '1d1d2d690cd7b24598f57368c4b0c42d, c71eabc1aa2afc175dc6d230971fd654, '
 '954eda25d58069ebe1001643f3680d26, b40cf06bb76299b1a21e970cd8d1c3b2, '
 '897173d0ca878a7f8b46929c89834f29, 4a73038642c37d5315c44c6307e5b688, '
 '65742e27f4c6c2d2da0ec5c50f1bac69, 63f8e9147bbf43573c95315b84d27c4f, '
 '2dfd307db4fc115e5e154df43deb78e1, 35eacabdebb938462bf9fe60665cb265, '
 'ae361f41f88957f957e4c5036d4d23c7, 624fa7c4df8d1068efc86c4ad2401396, '
 '90ad0ce8ff8a5f7958f31503fbbb476c, b49fe827d205b2ebd9e2b868507d7fce, '
 'a882ca97b85ba98ea294a94887dc7ec2, b89140b48b0dcdbcab984b7e22d3f273, '
 'f221c8c0a9cf6a9ed9bf9d62a928a34b, 663c69a62d44194206a7d5af924ed6c4, '
 'ae5dd0e79623d785e0646729d26342ce, 26f81e9f44742530d7d32db783180fb6, '
 'a8aee7211a2c178a556a20fd122ebbff, 1acd32806569c841fee85329bfaa6c4b, '
 'f1d1eab9b51459cedd1e263937d8d4b5, 5138a7ec14caf4d3938e9235091a6191, '
 'ef21b16f3039a66959f7becd696a1f66, e14c281041518365e0a909a0ebaeb3e9, '
 '242e507d2ef69c9936ba587b83c1ae91, 9c29319872c5b50b4263853ab0c9505b, '
 '1e1d62c83579d3689e70e3edd93abd45, 474827eee849f7d12d60a5277532d4bd, '
 '1cf0891816298a96f2d15711a6a4ad09, aa9ebe2e9dbfdb6fc7b6c000ed348c8d, '
 'c83c031cfc8ae13296f298e3cd1e432b, e03a4fb4a70490791c28e7a99432a4a0, '
 '718c84bd0a868763eed972f0c960154e,  are the md5 hash values generated for '
 'time interval 20:30:00.000000 to 20:50:00.000000')

#This test is similar to test 5 but the hash value has been changed to test out the hash value that is being generated.
def test6():
    date = "2022-10-24"
    time = "20:40:00.000"
    deltaTime = "10"
    pattern = "INFO"
    params = {'date': date, 'time': time, 'deltaTime': deltaTime, 'pattern': pattern}
    response = requests.get(awsLink, params=params)
    assert (response.text != "23dd84f54f17649e2ffa6ac2b950 is the md5 hash value generated for time interval 20:30:00.000000 to 20:50:00.000000")
