import randominfo
import pytest


person = randominfo.Person()

print(person.full_name)
print(person.gender)
print(person.address)
print(person.country)


# class TestRandomizer:
#     def test_fullname(self):
#         result = person.full_name
#         assert result is not None and result != "", "Error: full_name() did not return a valid value"
#
#     def test_gender(self):
#
#         result = person.gender
#         assert result is not None and result != "", "Error: gender() did not return a valid value"
#
#     def test_address(self):
#         result = person.address
#         assert result is not None and result != "", "Error: address() did not return a valid value"
#
#     def test_country(self):
#         result = person.country
#         assert result is not None and result != "", "Error: country() did not return a valid value"
