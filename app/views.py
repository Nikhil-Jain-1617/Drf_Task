from app.models import Category, Product
from app.serializers import CategorySerializer, ProductSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response



class CategoryApi(APIView): 

    def post(self, request):                                            #Create
        serializer = CategorySerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)                    
        
        
    
    def get(self, request):                                                         #Retrieve Info
        qs = Category.objects.all()
        ser = CategorySerializer(qs, many=True)
        return Response(ser.data)

    


    def put(self, request):
        id = request.POST.get("id")        
        category = request.POST.get("category")        
        try:
            qs = Category.objects.get(id=id)
            if qs:
                qs.category = category
                qs.save()
                resp = {
                    'success' : 'true',
                    'message' : "Category Has Been Successfully Updated",
                }
                return Response(resp, status=status.HTTP_201_CREATED)
        except:
            resp = {
                'success' : 'false',
                'message' : "Something went wrong please try again later",      
                }    
        return Response(resp, status=status.HTTP_304_NOT_MODIFIED)

    def delete(self, request):
        id = request.POST.get("id")  
        try:           
            qs = Category.objects.get(id=id).delete()
            if qs:
                resp = {
                    'success' : 'true',
                    'message' : "Category Deleted",
                    }
                return Response(resp, status=status.HTTP_200_OK)
        except:
            resp = {
                'success' : 'false',
                'message' : "Record does not exist",        }    
            return Response(resp, status=status.HTTP_400_BAD_REQUEST) 



class ProductApi(APIView):
   

    #Create Product
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


     #Retrieve Product    
    def get(self, request):
        qs = Product.objects.all()
        ser = ProductSerializer(qs, many=True)
        return Response(ser.data)
    
    #Update Product
    def put(self, request):
        id = request.POST.get("id")       
        product_name = request.POST.get("product_name")
        product_id = request.POST.get("product_id")
        product_model = request.POST.get("product_model")
        product_price = request.POST.get("product_price")    
        try: 
            qs = Product.objects.get(id=id)
            if qs:
                qs.product_name = product_name
                qs.product_id = product_id
                qs.product_model = product_model
                qs.product_price = product_price
                qs.save()
                resp = {
                    'success' : 'true',
                    'message' : "Product Has Been Successfully Updated",
                }
                return Response(resp, status=status.HTTP_201_CREATED)
        except:
            resp = {
                'success' : 'false',
                'message' : "Something went wrong please try again later",      
                }    
            return Response(resp, status=status.HTTP_304_NOT_MODIFIED) 

    
    #Delete Product
    def delete(self, request):
        id = request.POST.get("id")  
        try:           
            qs = Product.objects.get(id=id).delete()
            if qs:
                resp = {
                    'success' : 'true',
                    'message' : "Product Deleted",
                }
                return Response(resp, status=status.HTTP_200_OK)
        except:
            resp = {
                'success' : 'false',
                'message' : "Record does not exist",        }    
            return Response(resp, status=status.HTTP_400_BAD_REQUEST) 
