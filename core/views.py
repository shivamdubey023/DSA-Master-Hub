from django.shortcuts import render

def arrays(request):
    result = None 
    error = None


    if request.method == "POST":
        numbers = request.POST.get("numbers")

        if not  numbers:
            error = "Input cannot be empty"
        else:
            try: 
                number_list = [ 
                    int (num.strip())
                    for num in numbers.split(",")
                    if num.strip() != ""
                ]           
                number_list = list (map(int, numbers.split(",")))
                
                if len(number_list)<0:
                    error = "List cannot be empty"
                else: 
                    max_value = number_list [0]

            

                    i = 1
                    while i< len(number_list):
                      if number_list[i]> max_value:
                        max_value = number_list[i]
                        i+=1

                    result = f"Maximum value is {max_value}"

            except ValueError:
                error = "Only integer are allowed"

            

    return render (request, 'arrays.html',{
        "result": result,
        "error" : error
    })
            