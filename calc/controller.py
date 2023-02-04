import view
import model 

def button_click():

    my_list = view.get_equation()
    example = model.change_equation(my_list)
    result = model.calculation(example)
    view.print_result(result)


    
