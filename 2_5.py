def m_to_km (metre):
    return int(metre / 1000)
metre = float(input('Enter metre '))
print(f'{metre}m = {m_to_km(metre)}km')
