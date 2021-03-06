## डॉट टाइमर तयार करणे

टाइमर तयार करण्याचा आणखी एक मार्ग म्हणजे पिक्सल चे हिरवा रंग ऐवजी लाल रंग वापरणे.

+ डॉट टाइमर स्टार्टर ट्रिंकेट उघडा: <a href="http://jumpto.cc/dot-timer-go" target="_blank">jumpto.cc/dot-timer-go</a>

+ एक व्हेरिएबल `X` पिक्सेल बंद करण्यासाठी वापरा - त्यास आरजीबी मूल्यात लाल, हिरवा किंवा निळा नाही:
    
    ![स्क्रीनशॉट](images/timer-off.png)

+ `s` नावाचे व्हेरिएबल आपण मोजू इच्छित असलेल्या सेकंदांच्या संख्येसाठी वापरा.
    
    ![स्क्रीनशॉट](images/timer-seconds.png)

+ आपण Sense HAT ला 64 (8 × 8) रंगांची सूची देऊ शकता जेणेकरून वरच्या डावीकडून प्रारंभ करून आणि एकावेळी पंक्तीच्या खाली काम करत रंग प्रदर्शित करेल.
    
    आम्ही मोजू इच्छित असलेल्या प्रत्येक सेकंदासाठी हिरवा पिक्सेल बिंदू तयार करुन रंगांची यादी तयार करू आणि उर्वरित 64 पिक्सेल बंद राहतील. `timer` या व्हेरिएबलमध्ये प्रदर्शित करण्यासाठी रंगांची सूची आहे आणि रिक्त सुरू होते:
    
    ![स्क्रीनशॉट](images/timer-setup.png)

+ आता प्रत्येक सेकंदाला एक पिक्सेल लाल रंगवून काउंटडाउन चालवूया:
    
    ![स्क्रीनशॉट](images/timer-turn-red.png)

+ आपण पिक्सेल चालू आणि बंद करून **शेवटी** फ्लॅश देखील करू शकता:
    
    ![स्क्रीनशॉट](images/timer-flash.png)