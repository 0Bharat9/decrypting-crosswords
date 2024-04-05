from app import app
from flask import render_template as rt, request , session
from flask_login import login_required
from crosswords.modal import puzzle_data, blocked_cells, open_cells

     

##### .......................................... Crossword Routes  .............................................#####



@app.route('/veiw_crosswords/<int:page_number>' )
@login_required
def veiw_crossword(page_number):

    all_objects =[]
    for i in range (10746 ,16746):
        all_objects.append(i)
    start_index = (page_number - 1) * 9
    end_index = start_index + 9
    objects_to_display = all_objects[start_index:end_index]

    total_objects = len(all_objects)
    objects_per_page = 9
    total_pages, remainder = divmod(total_objects, objects_per_page)
    if remainder > 0:
        total_pages += 1
        
    return rt('veiw-crossword.html', objects=objects_to_display, page_number=page_number , total_pages =total_pages )




@app.route('/crossword', methods = ["POST"])
def crossword():
    if (request.method == "POST"):
        crosswordid = int(request.form.get("crossword-id"))
        session["crossword_id"] = crosswordid
        clue_data=puzzle_data(crosswordid)
        blocked_cell_list , inputId_clueId = blocked_cells(clue_data)
        list_open_cells , x = open_cells(clue_data)

            


    return rt('crossword.html', blocked_cell_list = blocked_cell_list, clue_data=clue_data , list_open_cells=list_open_cells )
