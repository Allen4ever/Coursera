text = "X-DSPAM-Confidence:    0.8475";
num=text[text.find('0'):text.find('5')+1]
print(float(num))
