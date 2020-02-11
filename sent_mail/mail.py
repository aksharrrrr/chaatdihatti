from flask import Flask
from flask_mail import Mail,Message
import yaml

app = Flask(__name__)
db = yaml.load(open('db.yaml'))
mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": db['EMAIL'], #enter gmail Id here
    "MAIL_PASSWORD": db['EMAIL_PASS']   #enter your password
}

app.config.update(mail_settings)
mail = Mail(app)

def smail(recipient):
    with app.app_context(), app.open_resource("sent_mail.rar") as fp:
        msg = Message(subject="Proposal: CHAAT DI HATTI",
        sender=app.config.get("MAIL_USERNAME"),
        recipients=[recipient],  #enter receivers email id
        body="Dear Sir\nGreetings for the day...\n\nIt was nice speaking to you sometime back tack this opportunity to thank you for showing your interest in becoming a franchisee of Chaat Di Hatti(The Chaat Store)\n\nWe would be happy to partner you at your location...!!\n\nThe Chaat Di Hatti concept is made with an idea of making the all time favourite Indian ethnic chaats & fast food snacks hygienic and standardized. We want to make reach the Indian ethnic food all over the world maintaining its mouth watering yummy taste but in a better way. The Chaat Di Hatti range of products includes wide range of mouth watering Gupchup or Pani-Puri, Traditional and Innovative range of Chaats, Variety of Bhel, Pav Bhaji, Pasta, Tikkis, Indian ethnic snacks, beverages and many more...\n\nIf you have passion for food we are always there to help you and guide you.\n\nPlease go through the details of the Total investments to start the franchisee.\n\n1) Franchisee Fee: Rs.2,00,000/- (+GST)\n2) Cost of Equipments(Approx.): Rs.1,25,000/-\n3) Interior Cost: Rs.1,50,000/-\n\nKindly find the enclosed attachments.\n\n1)Logo\n2)PPT Presentation\n3)Equipment pricing list\n4)Frnchisee application form\n5)Product Photography\n6)Main Branch Interior\n7)Chaat Di Hatti Menu Card\n8)ROI Sheet\n\nWarm Regards,\nChaat Di Hatti\n\nEmail:solidutilityllp.rajkot2019@gmail.com\nContact: 9723558558 ")   # enter messsage here                             
        msg.attach("sent_mail.rar", "file/rar", fp.read())
        #msg.attach("Presentation CDH.pdf", "file/pdf", fp2.read())
        #msg.attach("EQ._List_Chaat_Di_Hatti.xlsx", "file/xlsx", fp3.read())
        #msg.attach("CDH_Franchisee_Application_Form.docx", "file/docx", fp4.read())
        #msg.attach("PRODUCTS CDH.pdf", "file/pdf", fp5.read())
        #msg.attach("Interior CDH.pdf", "file/pdf", fp6.read())
        #msg.attach("Chaat di Hatti Menu.pdf", "file/pdf", fp7.read())
        #msg.attach("ROI_CDH.xls", "xls", fp8.read())
        mail.send(msg)


if __name__ == '__main__':
    app.run(debug=True)
 
        
        