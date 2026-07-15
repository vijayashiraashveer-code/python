import math

def calculate_trig_values(degrees):
   
    radians = math.radians(degrees)
    
  
    sine_val = math.sin(radians)
    cosine_val = math.cos(radians)
    
  
    if degrees % 180 == 90:
        tangent_val = "Undefined"
    else:
        tangent_val = math.tan(radians)
        

    print(f"\n--- Results for {degrees}° ---")
    print(f"Sin({degrees}°) = {sine_val:.4f}" if isinstance(sine_val, float) else f"Sin({degrees}°) = {sine_val}")
    print(f"Cos({degrees}°) = {cosine_val:.4f}" if isinstance(cosine_val, float) else f"Cos({degrees}°) = {cosine_val}")
    print(f"Tan({degrees}°) = {tangent_val:.4f}" if isinstance(tangent_val, float) else f"Tan({degrees}°) = {tangent_val}")


try:
    angle = float(input("Enter the angle in degrees: "))
    calculate_trig_values(angle)
except ValueError:
    print("Please enter a valid numerical value for the angle.")
