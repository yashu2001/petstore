from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse,JsonResponse
from rest_framework.permissions import IsAuthenticated
from .models import pet,owner
# Create your views here.
class pets_api(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self,request,pet_id=''):
        '''this method is used to insert new pets either for new owners or for existing owners'''
        try:
            if(owner.objects.all().filter(name=request.data['o_name']).filter(ph=request.data['ph']).exists()):#this condition checks if the owner is already present in our database
                new_pet=pet(name=request.data['name'],age=request.data['age'],breed=request.data['breed'],pet_type=request.data['pet_type'],owner=owner.objects.all().filter(name=request.data['o_name']).filter(ph=request.data['ph'])[0],sex=request.data['sex'])#creating new pet object with the characteristics or attributes sent in the body of the post request
                new_pet.save()#saving the newly created pet object
            else:
                o_object=owner(name=request.data['o_name'],ph=request.data['ph'],email=request.data['email'],address=request.data['address'])#this creates a new object for the owner 
                o_object.save()
                new_pet=pet(name=request.data['name'],age=request.data['age'],breed=request.data['breed'],pet_type=request.data['pet_type'],owner=owner.objects.all().filter(id=o_object.id)[0],sex=request.data['sex'])#creating new pet object
                new_pet.save()
                
            return JsonResponse('message:success',status=201,safe=False)
        except Exception as e:
            #print(e)
            return JsonResponse("message:fail",status=400,safe=False)
    def get(self,request,pet_id=''):
        if(len(pet_id)>=1 and pet_id!='all'):#check for parameter
            #this block is for returning a single pets details given the pet id
            try:
                qs=pet.objects.all().filter(id=int(pet_id))
                d=[]
                for x in qs:
                    a={}
                    a['name']=x.name
                    a['age']=x.age
                    a['breed']=x.breed
                    a['pet_type']=x.pet_type
                    a['sex']=x.sex
                    d.append(a)
                return JsonResponse(d,safe=False,status=200)
            except:
                return JsonResponse("message:failed to fetch",safe=False,status=400)

        elif(pet_id=='all'):  
            #this block is for returning name and id for all pets
            try:
                qs=pet.objects.all()
                d=[]
                for x in qs:
                    a={}
                    a['name']=x.name
                    a['id']=x.id
                    d.append(a)
                return JsonResponse(d,status=200,safe=False)
            except:
                return JsonResposne("message:failed to fetch",status=400,safe=False) 
    def delete(self,request,pet_id):
        '''this method is for deleting a pets detials'''
        try:
            qs=pet.objects.all().filter(id=int(pet_id)).delete() 
            return JsonResponse("message:success",safe=False,status=200)
        except:
            return JsonResponse("message:failed",safe=False,status=400)
    def put(self,request,pet_id):
        '''this method is for updating a pets details'''
        try:
            up_pet=pet.objects.all().filter(id=pet_id)
            print(request.data)
            for x,y in request.data.items():
                if(x=='name'):
                    print(x)
                    up_pet.update(name=y)
                elif(x=='age'):
                    print(x)
                    up_pet.update(age=y)
                elif(x=='breed'):
                    print(x)
                    up_pet.update(breed=y)
                elif(x=='pet_type'):
                    print(x)
                    up_pet.update(pet_type=y)
                elif(x=='sex'):
                    print(x)
                    up_pet.update(sex=y)      
            return JsonResponse("message:success",safe=False,status=200)
        except Exception as e:
            #print(e)
            return JsonResponse("message:failed",safe=False,status=400)
class ownerlist(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        '''this method is used to get list of all owners'''
        try:
            qs=owner.objects.all()
            d=[]
            for x in qs:
                a={}
                a['name']=x.name
                a['ph']=x.ph
                a['address']=x.address
                a['email']=x.email
                a['id']=x.id
                d.append(a)
            return JsonResponse(d,status=200,safe=False)
        except:
            return JsonResponse("message:failed to fetch",status=400,safe=False)
class petowner(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request,pet_id):
        '''this method is used to get owner details of a particular pet'''
        try:
            qs=pet.objects.all().filter(id=int(pet_id))
            d=[]
            for x in qs:
                a={}
                a['name']=x.owner.name
                a['ph']=x.owner.ph
                d.append(a)
            return JsonResponse(d,safe=False,status=200)
        except:
            return JsonResponse("message:failed to fetch",safe=False,status=400)
class ownerpets(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request,o_id):
        '''this method is used to get all pets of an owner'''
        try:
            qsu=pet.objects.all().filter(owner=owner.objects.all().filter(id=o_id)[0])
            d=[]
            for x in qsu:
                a={}
                a['name']=x.name
                a['breed']=x.breed
                a['age']=x.age
                a['pet_type']=x.pet_type
                a['id']=x.id
                d.append(a)
            return JsonResponse(d,safe=False,status=200)    
        except:
            return JsonResponse("message:failed to fetch",safe=False,status=400)


        