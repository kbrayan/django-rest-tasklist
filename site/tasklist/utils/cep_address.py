
import typing

from correios.client import Correios
from correios.models.address import ZipCode, ZipAddress
from correios.models.user import Service, User



# def find_zipcode(self, zip_code: Union[ZipCode, str]) -> ZipAddress:
#     zip_address_data = self._call("consultaCEP", str(zip_code))
#     return self.model_builder.build_zip_address(zip_address_data)

def get_zip_address(cep):
    client = Correios
    address = client.find_zipcode(ZipCode(cep))
    return address

# def request_tracking_codes(self, user: User, service: Service, quantity=1, receiver_type="C") -> list:
#     result = self._auth_call("solicitaEtiquetas",
#                                 receiver_type, str(user.federal_tax_number),
#                                 service.id, quantity)
#     return self.model_builder.build_tracking_codes_list(result)

# def get_tracking_codes(service, quantity):
#     olist_user = User("Your Company's Name", "Your Company's CNPJ")
#     client = Correios("Your Correio's username", "Your correio's password")
#     tracking_codes = client.request_tracking_codes(olist_user, Service.get(service), quantity=quantity)
#     print(tracking_codes)


