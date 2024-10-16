def clean_phone_inputs(phone_input):
    phone = str(phone_input).replace(' ', '').replace('(', '').replace(')', '').replace('-', '').replace('+1', '')
    return phone