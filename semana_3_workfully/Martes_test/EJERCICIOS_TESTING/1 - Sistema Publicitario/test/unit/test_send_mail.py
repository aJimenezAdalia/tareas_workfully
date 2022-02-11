

import unittest
from src.utils import send_mail

class TestSendMail(unittest.TestCase):

    # Wrong destinatary
    def test_mail_destinatary(self):
        result = send_mail(to='a.jimenez',
                           message='mensaje',
                           subject='nuestra_empresa')

        self.assertEqual(result, "E-mail sent")

    # Boolean Message
    def test_mail_message(self):
        result = send_mail(to='hola1234@gmail.com',
                           message=True,
                           subject='Empresa de Prueba')

        self.assertEqual(result, "E-mail sent")



if __name__ == '__main__':
    unittest.main()