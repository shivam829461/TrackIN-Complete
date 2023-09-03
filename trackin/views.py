from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
from track.models import Track,Lead
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from geopy.geocoders import Nominatim
from haversine import haversine




def index(request):
    
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

# def dynamic(request,dyna):
#     return HttpResponse(dyna)

def partner(request):
    return render(request,"partner1.html")

def track(request):
    # ref=""
    # try:
    #     if request.method=="POST":
    #         ref=request.POST['ref_no']
    #         print(ref)
    #         url='/ship/?out={}'.format(ref)
    #         # return HttpResponseRedirect(url)
            
    # except:
    #     pass
    return render(request,"track.html")

def ship(request):
    trackdata=Track.objects.all()
    try:
        if request.method=="POST":
            out=request.POST['ref_no']
            trackdata=Track.objects.filter(waybill=out)
            if trackdata.exists():

            
                d={
                    "trackin":trackdata
                }
                return render (request,"shipdetails.html",d)
            else:
                raise ObjectDoesNotExist
        # return render(request,"shipdetails.html",{"waybill":out})
    except ObjectDoesNotExist:

        # return HttpResponse("No Data Found")
        return render(request,"notfound.html")


def services(request):
    return render(request,"services.html")


def shipwithus(request):
    if request.method=="POST":
        typ=request.POST["type"]
        fname=request.POST["Fname"]
        lname=request.POST["Lname"]
        add1=request.POST["address1"]
        add2=request.POST["address2"]
        city=request.POST["city"]
        state=request.POST["state"]
        pin=request.POST["zip"]
        country=request.POST["country"]
        phone=request.POST["phone"]
        email=request.POST["email"]
        feedback=request.POST["feedback"]

        leads=Lead(type=typ, fname=fname, lname=lname,address1=add1,address2=add2,city=city,state=state,pin=pin,country=country, phone=phone, email=email,feedback=feedback)   
        leads.save()

        msg="Dear {},\n\nWe would like to express our sincere gratitude for trying our logistics platform, Trackin. Your support means a lot to us, and we hope that you found our services helpful and efficient.\nShould you have any feedback or further inquiries, please feel free to reach out to our dedicated team. \nThank you once again for choosing Trackin! \n\n\nBest regards,\nShivam Sharma, \nTrackin Team".format(fname)


        send_mail(
        "Track_IN",
        msg,
        "trackin.com@gmail.com",
        [email],
        fail_silently=False,
        )


        return render(request,"leadsuccess.html")
    return render(request,"shipwithus.html")


def mapdetails(request):
    return render(request,"mapdetails.html")


# views.py

def get_cities(request):
    if request.method=="POST":
        typ=request.POST["type"]
        articleType=request.POST["articleType"]
        city1=request.POST["from"]
        state1=request.POST["state1"]
        city2=request.POST["city2"]
        # state2=request.POST["state2"]
        country=request.POST["country"]
        weight=request.POST["weight"]

        geolocator = Nominatim(user_agent="city_coordinates_app")

   
        city_1=f"{city1}"
        city_2=f"{city2}"

        try:
            # Perform geocoding
            location1 = geolocator.geocode(city_1)
            location2 = geolocator.geocode(city_2)
            
            if location1 and location2:
                latitude1 = location1.latitude
                longitude1 = location1.longitude

                latitude2 = location2.latitude
                longitude2 = location2.longitude


                coords_1 = (latitude1, longitude1)
                coords_2 = (latitude2, longitude2)

                # Calculate distance using haversine formula
                distance = haversine(coords_1, coords_2)
                time=3
                t_dis=int(distance)
                if t_dis>500 and t_dis<1000:
                    time=7
                elif t_dis>1000 and t_dis<1500:
                    time=9
                elif t_dis>1500:
                    time=15
                
                


                postage=0
                # a=(f"Coordinates for {location1}: Latitude={latitude1}, Longitude={longitude1}")
                # b=(f"Coordinates for {location2}: Latitude={latitude2}, Longitude={longitude2}")
                if typ=="International":
                    time=30
                    base_rate_per_km = 5.0 
                    weight_rate = 18.0 
                    postage = (int(distance) * base_rate_per_km) + (float(weight) * weight_rate **2)
                else:

                    base_rate_per_km = 0.7
                    weight_rate = 18.0      
                    postage = (int(distance) * base_rate_per_km) + (float(weight) * weight_rate )+50

                
                
                postage=f"{postage:.2f}"
                distance=f"{distance:.2f}"
            else:
                if not location1:
                    return HttpResponseNotFound(f"Coordinates for {city_1 } not found.")
                else:
                    return HttpResponseNotFound(f"Coordinates for {city_2 } not found.")

        except Exception as e:
            return HttpResponseNotFound(f"An error occurred: {str(e)}")
        
        print(type(distance))
        return render(request, "postage_details.html", {"weight":weight,"distance":distance,"time":time,"postage":postage})
    
    indian_states = {
    'Andhra Pradesh': 'Amaravti',
    'Arunachal Pradesh': 'Itanagar',
    'Assam': 'Dispur',
    'Bihar': 'Patna',
    'Chhattisgarh': 'Raipur',
    'Goa': 'Panaji',
    'Gujarat': 'Gandhinagar',
    'Haryana': 'Chandigarh',
    'Himachal Pradesh': 'Shimla',
    'Jharkhand': 'Ranchi',
    'Karnataka': 'Bengaluru',
    'Kerala': 'Thiruvananthapuram',
    'Madhya Pradesh': 'Bhopal',
    'Maharashtra': 'Mumbai',
    'Manipur': 'Imphal',
    'Meghalaya': 'Shillong',
    'Mizoram': 'Aizawl',
    'Nagaland': 'Kohima',
    'Odisha': 'Bhubaneswar',
    'Punjab': 'Chandigarh',
    'Rajasthan': 'Jaipur',
    'Sikkim': 'Gangtok',
    'Tamil Nadu': 'Chennai',
    'Telangana': 'Hyderabad',
    'Tripura': 'Agartala',
    'Uttar Pradesh': 'Lucknow',
    'Uttarakhand': 'Dehradun',
    'West Bengal': 'Kolkata'
    }
    article_types = {
    'Letter/Document': "Letter",
    'Electronics': 'Electronic devices and components',
    'Clothing': 'Clothes and apparel',
    'Furniture': 'Furniture items and home decor',
    'Books': 'Printed and digital books',
    'Food': 'Perishable and non-perishable food items',
    'Automotive': 'Vehicle parts and accessories',
    'Jewelry': 'Precious and costume jewelry',
    'Healthcare': 'Medical equipment and supplies',
    'Home Appliances': 'Household appliances',
    'Musical Instruments': 'Musical instruments and accessories',
    'Office Supplies': 'Stationery and office products',
    'Electrical Equipment': 'Electrical wiring and components',
    'Construction Materials': 'Building and construction materials',
    'Outdoor Gear': 'Camping and outdoor adventure equipment',
    'Antiques': 'Antique and vintage items',
    'Fitness Equipment': 'Exercise and fitness gear',
    }



    
    
    return render(request,"postage.html",{'indian_states': indian_states,'article_types': article_types})

