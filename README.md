# Vigenère Cipher Cracker
`vigenere_cipher_crack_tool.py` is a script that breaks cipher texts encrypted with `Vigenère Cipher`,
without knowing the key length or any additional information.

## Getting Started
### Prerequisites
```
Python version >= 3.8
pip install requirements.txt
```

* Run `vigenere_cipher_crack_tool.py` and enter a cipher text
* The cipher text must only consist of plain English letters
* Special characters and numbers are not considered in this example
* The results will be printed on the console as well as created in a file called `results.txt` inside a folder named `plaintext`
* To break a cipher text, it is recommended to use long ciphers to get more accurate analysis results of intervals and frequencies
* This is not the case when encrypting or decrypting texts using `vigerene_cipher_tool.py` with a known secret key

### Concept
The technique is based on calculating the `Index of Coincidence` and then performing cryptanalysis or `frequency analysis`
on the cipher letters then comparing it to the frequency of the English letters and aligning those frequencies together.

Few possible keywords are generated, and their corresponding possible plain texts as well. The plain texts are tested against common English words,
 and the one that has the highest rate of common English words found `(e.g. has, was, she)`, is likely to be the result.

Below are two different cipher texts encrypted with `Vigenère Cipher`. 
Try them and find out the key and the plaint text:

```
Cipher 1:
QRBAI UWYOK ILBRZ XTUWL EGXSN VDXWR XMHXY FCGMW WWSME LSXUZ MKMFS BNZIF YEIEG RFZRX WKUFA XQEDX DTTHY NTBRJ LHTAI KOCZX QHBND ZIGZG PXARJ EDYSJ NUMKI FLBTN HWISW NVLFM EGXAI AAWSL FMHXR SGRIG HEQTU MLGLV BRSIL AEZSG XCMHT OWHFM LWMRK HPRFB ELWGF RUGPB HNBEM KBNVW HHUEA KILBN BMLHK XUGML YQKHP RFBEL EJYNV WSIJB GAXGO TPMXR TXFKI WUALB RGWIE GHWHG AMEWW LTAEL NUMRE UWTBL SDPRL YVRET LEEDF ROBEQ UXTHX ZYOZB XLKAC KSOHN VWXKS MAEPH IYQMM FSECH RFYPB BSQTX TPIWH GPXQD FWTAI KNNBX SIYKE TXTLV BTMQA LAGHG OTPMX RTXTH XSFYG WMVKH LOIVU ALMLD LTSYV WYNVW MQVXP XRVYA BLXDL XSMLW SUIOI IMELI SOYEB HPHNR WTVUI AKEYG WIETG WWBVM VDUMA EPAUA KXWHK MAUPA MUKHQ PWKCX EFXGW WSDDE OMLWL NKMWD FWTAM FAFEA MFZBN WIHYA LXRWK MAMIK GNGHJ UAZHM HGUAL YSULA ELYHJ BZMSI LAILH WWYIK EWAHN PMLBN NBVPJ XLBEF WRWGX KWIRH XWWGQ HRRXW IOMFY CZHZL VXNVI OYZCM YDDEY IPWXT MMSHS VHHXZ YEWNV OAOEL SMLSW KXXFX STRVI HZLEF JXDAS FIE

cipher 2:
DAZFI SFSPA VQLSN PXYSZ WXALC DAFGQ UISMT PHZGA MKTTF TCCFX KFCRG GLPFE TZMMM ZOZDE ADWVZ WMWKV GQSOH QSVHP WFKLS LEASE PWHMJ EGKPU RVSXJ XVBWV POSDE TEQTX OBZIK WCXLW NUOVJ MJCLL OEOFA ZENVM JILOW ZEKAZ EJAQD ILSWW ESGUG KTZGQ ZVRMN WTQSE OTKTK PBSTA MQVER MJEGL JQRTL GFJYG SPTZP GTACM OECBX SESCI YGUFP KVILL TWDKS ZODFW FWEAA PQTFS TQIRG MPMEL RYELH QSVWB AWMOS DELHM UZGPG YEKZU KWTAM ZJMLS EVJQT GLAWV OVVXH KWQIL IEUYS ZWXAH HUSZO GMUZQ CIMVZ UVWIF JJHPW VXFSE TZEDF
```

#### Note:
You could also look into an easier way of getting the keyword, using `Chi-Squared statistic` based on letter count as opposed to letter probability.

### Checkout a list of useful links: 
* [Chi Squared statistic](http://practicalcryptography.com/cryptanalysis/text-characterisation/chi-squared-statistic/)
* [Cryptanalysis Using n-gram](http://nob.cs.ucdavis.edu/classes/ecs155-2013-04/extras/vigenere.html)
* [Index of Coincidence (1)](http://www.crypto-it.net/eng/theory/index-of-coincidence.html)
* [Index of Coincidence (2)](https://pages.mtu.edu/~shene/NSF-4/Tutorial/VIG/Vig-IOC.html)
* [Cryptanalysis on Vigenere Cipher](http://practicalcryptography.com/cryptanalysis/stochastic-searching/cryptanalysis-vigenere-cipher/)


# Vigenère Cipher
The other script `vigenere_cipher_tool.py` is just a simple algorithm that allows you to decipher and encipher cipher texts and plain texts,
with a known `secret key`

## Getting Started
* Run the script, and enter the one of the options displayed
```
1. Encrypt
2. Decrypt
3. Exit
```
* Enter your plain text or cipher text, and a secret key. The results will be printed on the console
* The script only supports plain English letters, no special characters or numbers
