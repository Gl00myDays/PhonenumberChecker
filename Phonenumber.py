import phonenumbers
from phonenumbers import geocoder, carrier, timezone, PhoneNumberType

# Prompt the user to enter the filename
filename = input("Enter your List: ")

# Open the text file containing phone numbers
with open(filename, "r") as file:
    phone_numbers = file.read().splitlines()

# Open the output file to save the results
output_file = input("Enter filename Saved: ")

with open(output_file, "w", encoding="utf-8") as output:
    # Loop through each phone number
    for index, number in enumerate(phone_numbers, 1):
        PhoneN = phonenumbers.parse(number)
        Carrier = carrier.name_for_valid_number(PhoneN, 'en')
        Location = geocoder.description_for_number(PhoneN, 'en')
        Time = timezone.time_zones_for_number(PhoneN)
        number_type = phonenumbers.number_type(PhoneN)
        if number_type == 2:
            typenumber = "Fixed Line"
        else:
            typenumber = "Mobile"
        # Format the results for each phone number
        result = "{}. Phone number: {}, Carrier: {}, Location: {}, Timezone: {}, NumberType:{}\n".format(index, PhoneN, Carrier, Location, Time,typenumber)
        save = "{}|{}|{}\n".format(number, Carrier, Location)
        
        # Print the results
        print(result)
        
        # Write the results to the output file
        if number_type == 1:
            output.write(save)
        else:
            pass
