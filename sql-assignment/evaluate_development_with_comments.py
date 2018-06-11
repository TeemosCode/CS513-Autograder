import sql_util as su
#import traceback as tb
import math
import sys
import metadata_reader

## Used to make the auto-grader able to grade files under sub-folders in the 'solutions' folder
import os
import shutil



def evaluate(mr, print_feedback_to=None):
    total_score = 0
    results = {}
    problem_names = mr.problem_names()
    for problem_name in problem_names:
        score = evaluate_problem(problem_name, mr, print_feedback_to)
        results[problem_name] = score
        total_score += score
        print_output("___________________________________________________________________________", print_feedback_to)
    total_score = int(math.ceil(total_score))
    print_output("Total Score: {0}/{1}".format(total_score, mr.total_marks()), print_feedback_to)
    return results, total_score


def evaluate_problem(problem_name, mr, print_feedback_to):
    print_output("Evaluating problem: {0}".format(problem_name), print_feedback_to)
    score = 0.0
    expected_output_file = mr.expected_output_file_path(problem_name)
    database_file = mr.database_path(problem_name)


    query_file = mr.query_file_path(problem_name)   #### Solution .sql files inside Solutions   # solutions/problem.sql ....
    sort_before_comparison = mr.sort_before_comparison(problem_name)
    try:
        passed = su.cmp_select_output_with_csv(expected_output_file, database_file, query_file, sort_before_comparison)
        if passed:
            score = mr.score_fraction(problem_name)*mr.total_marks()
            print_output("\tYour output matches with expected output. Score={0}".format(score), print_feedback_to)
        else:
            print_output("\tYour output doesn't match with expected output. Score={0}".format(score), print_feedback_to)
    except Exception as e:
        print_output("\t" + e.message + "Score={0}".format(score), print_feedback_to)
        #tb.print_exc(file=print_feedback_to)
    return score


def print_output(message, print_feedback_to):
    print >> print_feedback_to, message


# Self Added Helper function to list out all files or directories underneath a path and also ignore hidden files
def dir_file_ingore_hidden_files_list(dir_path):
    return [file_or_dir for file_or_dir in os.listdir(dir_path) if not file_or_dir.startswith(".")]

if __name__ == "__main__":
    solutions_dir = "solutions"
    config_file = "grading_config.json"


    ###### Code to try fixing the problem where the auto-grader would not grade provided answers that are not directly
    #### under the 'solutions' directory
    try:
        # Listing out all files or directories inside the solutions dir (ignoring all hidden files that start with ".")
        dir_file_checklist = dir_file_ingore_hidden_files_list(solutions_dir)

        print "  \nList of submitted files for grading:\n", dir_file_checklist, "\n==========================================================================="

        # When there is another subdirectory containing the actual answer files provided by the students (when students
        # zipped another directory in their zip file)
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), solutions_dir + "/" + dir_file_checklist[0])
        if len(dir_file_checklist) == 1 and os.path.isdir(path):
            print("Please zip all the answers under EXACTLY ONE zip file next time!!")
            print("Because your zip file had another folder with the answers within, the auto-grader will move all the\
            files one directory upwards and delete your original sub-folder so it could work with the auto-grader for successful\
            grading")
            print("Processing .....\n-------------------")
            # Get a list of all the answer files
            print("Extracting all answer files ...\n-------------------")
            answer_files = dir_file_ingore_hidden_files_list(path)
            print(answer_files)
            # Move all the answer files to the current directory (Where it should meet the requirement of the auto-grader)
            print("Moving all answer files to correct location for further grading\n-----------------")
            for files in answer_files:
                # Move the path names to the folder under solutions folder  The second argument is the path of "solutions"
                shutil.move(path + "/" + files, os.path.join(os.path.dirname(os.path.abspath(__file__)), solutions_dir))
            # then delete the sub-directory
            print("Deleting sub-folder .... \n-----------------")
            shutil.rmtree(path)
            print("FINISHED!")
    except:
        print("Please zip your answer files ALL UNDER ONE ZIP FOLDER!")

    ################# End of bug fixing Code #####################

    meta_reader = metadata_reader.JSONMetadataReader(config_file, solutions_dir)
    results_g, total_score_g = evaluate(meta_reader, sys.stdout)

