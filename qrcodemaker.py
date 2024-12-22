import qrcode

upi_id = input("Enter Your UPI Id:")

#DEFINING URLs
phonepe_url = f'upi://pay?pa={upi_id}&pn=Receipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Receipient%20Name&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Receipient%20Name&mc=1234'

#CREATE QR CODES FOR EACH APP
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr =  qrcode.make(google_pay_url)

#SAVE THE IMAGE OF QR CODE
phonepe_qr.save("phonepe_qr.png")
paytm_qr.save("paytm_qr.png")
google_pay_qr.save("google_pay_qr.png")

#DISPLAY THE QR CODE
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()

