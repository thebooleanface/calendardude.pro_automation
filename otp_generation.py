import pyotp

# Secret key for the OTP (this should be shared with the server)
secret_key = "TOTP"

# Create a TOTP object
totp = pyotp.TOTP(secret_key)

# Generate the current OTP
current_otp = totp.now()

# Print the OTP
print(f"Current OTP: {current_otp}")