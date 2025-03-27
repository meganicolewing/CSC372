#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>


//takes the name of the file containing the DIMACS standard SAT info
//reads all info from the file and returns an array of the rules, each rule on one line
void readfile(FILE* file, int** clauses, int num_rules);

//takes the SAT rules, the probability of a random walk, and the maximum number of changes
//performs walkSAT
//returns true if the SAT problem is satisfied in the given number of changes, false otherwise
int walkSAT(int** clauses, int num_clauses, int p, int max_walk, int num_symbols);

//takes all SAT clauses and the current assignment
//returns the number of false clauses
//returns the indices of all false clauses in false_clauses
int falseRules(int** clauses, int num_clauses, int* assignment, int* false_clauses);

//takes all SAT clauses, the current assignment, and the clause to inspect
//checks all flips of variables in clause to see which gives the most satisfied clauses
//edits assignment to flip that variable
//returns the number of clauses satisfied by the new assignment
int maxSat(int** clauses, int num_clauses, int* assignment, int clause);

//takes the SAT rules and symbols
//calls the recursive dpll function
//returns true if saisfiable, false otherwise
int dpllSAT(int** clauses, int num_clauses, int num_symbols);

//performs one step of dpll, returns true if satisfiable
//recursive
//bases cases: every rule is satisfied, one rule is false
//recursions: pure symbol, unit clause, or assign the next symbol
int dpll(int** clauses, int num_clauses, int* solution, int len_solution);

//takes the SAT rules and symbols and the current assignment
//if a variable only occurs in one value unsolved clauses, returns that value
//otherwise, returns 0
int findPureSymbol(int** clauses, int num_clauses, int* solution, int len_solution);

//takes the SAT rules and symbols and the current assignment
//if a variable occurs in a unit clause, returns that value
//otherwise, returns 0
int findUnitClause(int** clauses, int num_clauses, int* solution);

//takes the SAT rules and current dpll solution
//returns -1 if a clause is false based on the solution
//returns 1 if all clauses are true
//returns 0 otherwise
int dpllChecker(int** clauses, int num_clauses, int* solution);

//sets all the values of new_solution with the values if solution
//sets new_val in new_solution
//for recursion in dpll
void newSolution(int* solution, int len_solution, int new_val, int* new_solution);

void printSolution(int* solution, int len_sol);

int localSAT(int** clauses, int num_clauses, int max_walk, int num_symbols);


int main(){
    srand(time(NULL));
    char file_names[32][15] = {"f0020-01-s.cnf",
                            "f0020-01-u.cnf",
                            "f0020-02-s.cnf",
                            "f0020-02-u.cnf",
                            "f0020-03-s.cnf",
                            "f0020-03-u.cnf",
                            "f0020-04-s.cnf",
                            "f0020-04-u.cnf",
                            "f0020-05-s.cnf",
                            "f0020-05-u.cnf",
                            "f0020-06-s.cnf",
                            "f0020-06-u.cnf",
                            "f0020-07-s.cnf",
                            "f0020-07-u.cnf",
                            "f0020-08-s.cnf",
                            "f0020-08-u.cnf",
                            "f0040-01-s.cnf",
                            "f0040-01-u.cnf",
                            "f0040-02-s.cnf",
                            "f0040-02-u.cnf",
                            "f0040-03-s.cnf",
                            "f0040-03-u.cnf",
                            "f0040-04-s.cnf",
                            "f0040-04-u.cnf",
                            "f0040-05-s.cnf",
                            "f0040-05-u.cnf",
                            "f0040-06-s.cnf",
                            "f0040-06-u.cnf",
                            "f0040-07-s.cnf",
                            "f0040-07-u.cnf",
                            "f0040-08-s.cnf",
                            "f0040-08-u.cnf"

    };   
    int i = 0;                
    char* file_name;
    for(i = 0;i<32;i++){
        file_name = file_names[i];
        //file_name = "10.40.160707067.cnf";
        //file_name = "test.cnf";
        printf("file: %s\n",file_name);
        FILE *file = fopen(file_name,"r");
        if(file == NULL){
            printf("error opening file");
            exit(1);
        }
        int num_rules, num_vars;
        int ** clauses;
        char* buffer;
        fgets(buffer,100,file);
        fscanf(file,"p cnf %d %d\n",&num_vars,&num_rules);
        //printf("%d %d\n",num_vars,num_rules);
        clauses = malloc(num_rules*sizeof(int*));
        if(clauses==NULL){
            printf("error allocating rules");
            exit(1);
        }
        for(int i = 0; i<num_rules;i++){
            clauses[i] = malloc((num_vars+1)*sizeof(int));
            if(clauses[i]==NULL){
                printf("error allocating rules");
                exit(1);
            }
        }
        readfile(file,clauses,num_rules);
        fclose(file);
        //printSolution(clauses[0],4);
        //printf("DPLL:\n");
        clock_t before = clock();
        dpllSAT(clauses,num_rules,num_vars);
        clock_t after = clock();
        FILE* dplldata = fopen("dplldata.csv","a");
        fprintf(dplldata,"%s,%f\n",file_name,((double) (after - before)) / CLOCKS_PER_SEC);
        fclose(dplldata);
        /*
        int maxwalk = num_vars*num_vars;
        printf("local:\n");
        before = clock();
        int c = localSAT(clauses,num_rules,maxwalk,num_vars);
        after = clock();
        FILE* localdata = fopen("localdata.csv","a");
        fprintf(localdata,"%s,%f,%d\n",file_name,((double) (after - before)) / CLOCKS_PER_SEC,c);
        fclose(localdata);
        printf("walkSAT:\n");
        float avg_time = 0;
        float avg_c = 0;
        for(int j = 0;j<10;j++){
            printf("j=%d\n",j);
            before = clock();
            c = walkSAT(clauses,num_rules,60,maxwalk,num_vars);
            after = clock();
            avg_time += ((double) (after - before)) / CLOCKS_PER_SEC;
            avg_c += c;
        }
        avg_time = avg_time/10.0;
        avg_c = avg_c/10.0;
        FILE* walkdata = fopen("walksatdata.csv","a");
        fprintf(walkdata,"%s,%f,%f\n",file_name,avg_time,avg_c);
        fclose(walkdata);
        */
        for(int i =0;i<num_rules;i++){
            free(clauses[i]);
        }
        free(clauses);
    }
    
    return 0;
}

//takes the name of the file containing the DIMACS standard SAT info
//reads all info from the file and returns an array of the rules, each rule on one line
void readfile(FILE* file, int** rules, int num_rules){
   /* FILE *file = fopen(file_name,"r");
    if(file == NULL){
        printf("error opening file");
        exit(1);
    }
    printf("read");
    char* buffet;
    fgets(buffet,100,file);
    printf("%s\n",buffet);
    */
    //int num_rules, num_vars;
    //fscanf(file,"p cnf %d %d\n",&num_vars,&num_rules);
    //printf("%d %d\n",num_vars,num_rules);
    for(int i = 0;i<num_rules;i++){
        int buffer;
        int j = 0;
        do{
            fscanf(file,"%d",&buffer);
            rules[i][j] = buffer;
            //printf("%d ",buffer);
            j++;
        } while(buffer!=0);
        //printf("\n");
    }
}

//takes the SAT rules, the probability of a random walk, and the maximum number of changes
//performs walkSAT
//returns true if the SAT problem is satisfied in the given number of changes, false otherwise
int walkSAT(int** clauses, int num_clauses, int p, int max_walk, int num_symbols){
    int* solution = malloc(num_symbols*sizeof(int));
    int num_false;
    if(solution==NULL){
        printf("error allocating solution");
        exit(1);
    }
    for(int i = 1; i<=num_symbols;i++){
        int positive = rand()%2;
        if(positive){
            solution[i-1] = i;
        }
        else{
            solution[i-1] = -i;
        }
    }
    //printSolution(solution,num_symbols);
    for(int i =0; i<max_walk;i++){
        int* false_clause_arr = malloc(num_symbols*sizeof(int));
        num_false = falseRules(clauses,num_clauses,solution,false_clause_arr);
        if(num_false==0){
            printSolution(solution,num_symbols);
            free(solution);
            return num_symbols;
        }
        int chosen_clause = false_clause_arr[rand()%num_false];
        free(false_clause_arr);
        int probability = (rand()%100);
        if(probability<(p)){
            //printf("random walk\n");
            int* variables = malloc(num_symbols*sizeof(int));
            if(variables == NULL){
                printf("error allocating variables in walkSAT");
                exit(1);
            }
            int num_variables = 0;
            int curr_var = clauses[chosen_clause][0];
            while(curr_var!=0){
                //printf("curr: %d\n",curr_var);
                variables[num_variables] = curr_var;
                num_variables++;
                curr_var = clauses[chosen_clause][num_variables];
            }
            int chosen_var = variables[rand()%num_variables];
            solution[abs(chosen_var)-1] = -solution[abs(chosen_var)-1];
            free(variables);
        }
        else{
            //printf("greedy search\n");
            maxSat(clauses,num_clauses,solution,chosen_clause);
        }
        //printSolution(solution,num_symbols);
    }
    //printSolution(solution,num_symbols);
    free(solution);
    return num_symbols-num_false;
}

//takes all SAT clauses and the current assignment
//returns the number of false clauses
//returns the indices of all false clauses in false_clauses
int falseRules(int** clauses, int num_clauses, int* assignment, int* false_clauses){
    int num_false = 0;
    for(int i = 0; i<num_clauses; i++){
        int j = 0;
        int clause_sat = 0;
        int current_literal = clauses[i][0];
        while(!clause_sat && current_literal!=0){
            int current_var = abs(current_literal);
            if(assignment[current_var-1]==current_literal){
                clause_sat = 1;
            }
            j++;
            current_literal = clauses[i][j];
        }
        if(!clause_sat){
            false_clauses[num_false]=i;
            num_false++;
        }
    }
    return num_false;
}

//takes all SAT clauses, the current assignment, and the clause to inspect
//checks all flips of variables in clause to see which gives the most satisfied clauses
//edits assignment to flip that variable
int maxSat(int** clauses, int num_clauses, int* assignment, int fix_clause){
    int *chosen = clauses[fix_clause];
    int flip = 0;
    int best_flip = 0;
    int best_sat = 0;
    int i = 0;
    while(chosen[i]!=0){
        int var = abs(chosen[i]);
        int reset = assignment[var-1];
        int flip;
        if(chosen[i]>0){
            flip = var;
        }
        else{
            flip = -var;
        }
        assignment[var-1] = flip;
        int *false_clauses = malloc(num_clauses*sizeof(int));
        if(false_clauses==NULL){
            printf("error allocating false clauses ");
            exit(1);
        }
        int num_false = falseRules(clauses,num_clauses,assignment,false_clauses);
        free(false_clauses);
        int num_true = num_clauses-num_false;
        if(num_true>best_sat){
            best_sat = num_true;
            best_flip = flip;
        }
        assignment[var-1]=reset;
        i++;
    }
    assignment[abs(best_flip)-1] = best_flip;
    return best_sat;  
}

//takes the SAT rules and symbols
//calls the recursive dpll function
//returns true if saisfiable, false otherwise
int dpllSAT(int** clauses, int num_clauses, int num_symbols){
    int* solution = malloc(num_symbols*sizeof(int));
    for(int i = 0;i<num_symbols;i++){
        solution[i] = 0;
    }
    return dpll(clauses,num_clauses,solution,num_symbols);
}

//performs one step of dpll, returns true if satisfiable
//recursive
//bases cases: every rule is satisfied, one rule is false
//recursions: pure symbol, unit clause, or assign the next symbol
int dpll(int** clauses, int num_clauses, int* solution, int len_solution){
    //printf("new loop\n");
    //printSolution(solution,len_solution);
    int check = dpllChecker(clauses,num_clauses,solution);
    //printf("check: %d\n",check);
    if(check==1){
        //need to set all unset variables!!!!!!!!!!!!!!!!!!!!
        for(int i = 0;i<len_solution;i++){
            if(solution[i]==0){
                solution[i] = i+1;
            }
        }
        //printSolution(solution,len_solution);
        return 1;
    }
    else if(check == -1){
        return 0;
    }
    int pure_symbol = findPureSymbol(clauses,num_clauses,solution,len_solution);
    //printf("pure symbol: %d\n",pure_symbol);
    if(pure_symbol!=0){
        int* new_soln = malloc(len_solution*sizeof(int));
        newSolution(solution,len_solution,pure_symbol,new_soln);
        int solve = dpll(clauses,num_clauses,new_soln,len_solution);
        free(new_soln);
        return solve;
    }
    int unit_clause = findUnitClause(clauses,num_clauses,solution);
    //printf("unit clause: %d\n",unit_clause);
    if(unit_clause!=0){
        int* new_soln = malloc(len_solution*sizeof(int));
        newSolution(solution,len_solution,unit_clause,new_soln);
        int solve = dpll(clauses,num_clauses,new_soln,len_solution);
        free(new_soln);
        return solve;
    }
    int next_val = -1;
    int i = 0;
    while(next_val == -1 && i<len_solution){
        //printf("%d\n",solution[i]);
        if(solution[i] == 0){
            //printf("change next val\n");
            next_val = i+1;
        }
        i++;
    }
    //printf("next val: %d\n",next_val);
    int* new_soln1 = malloc(len_solution*sizeof(int));
    int* new_soln2 = malloc(len_solution*sizeof(int));
    newSolution(solution,len_solution,next_val,new_soln1);
    newSolution(solution,len_solution,-(next_val),new_soln2);
    //printSolution(new_soln1,len_solution);
    //printSolution(new_soln2,len_solution);
    int solve1 = dpll(clauses,num_clauses,new_soln1,len_solution);
    if(solve1==1){
        free(new_soln1);
        free(new_soln2);
        return 1;
    }
    int solve2 = dpll(clauses,num_clauses,new_soln2,len_solution);
    free(new_soln1);
    free(new_soln2);
    return solve2;

}

//takes the SAT rules and symbols and the current assignment
//if a variable only occurs in one value in unsolved clause, returns that value
//otherwise, returns 0
int findPureSymbol(int** clauses, int num_clauses, int* solution, int len_solution){
    //printf("pure symbol\n");
    int* symbols = malloc(len_solution*sizeof(int));
    if(symbols==NULL){
        printf("error allocating memory in pure symbol");
        exit(1);
    }
    for(int i =0; i<len_solution;i++){
        if(solution[i]==0){
            symbols[i]=0;
        }
        else{
            symbols[i] = len_solution+1;
        }
    }
    for(int i = 0; i<num_clauses;i++){
        int clause_sat = 0;
        int current_literal = clauses[i][0];
        int j = 0;
        while(current_literal!=0){
            int current_var = abs(current_literal);
            if(solution[current_var-1]==current_literal){
                clause_sat = 1;
            }
            j++;
            current_literal = clauses[i][j];
        }
        if(!clause_sat){
            current_literal = clauses[i][0];
            j = 0;
            while(current_literal!=0){
                int current_var = abs(current_literal);
                if(symbols[current_var-1]==0){
                    symbols[current_var-1] = current_literal;
                }
                else if(symbols[current_var-1]!=current_literal){
                    symbols[current_var-1] = len_solution+1;
                }
                j++;
                current_literal = clauses[i][j];
            }
        }
        //printSolution(symbols,len_solution);
    }
    for(int i = 0;i<len_solution;i++){
        if(symbols[i]!=len_solution+1){
            int ret_num = symbols[i];
            free(symbols);
            return ret_num;
        }
    }
    free(symbols);
    return 0;
}

//takes the SAT rules and symbols and the current assignment
//if a variable occurs in a unit clause, returns that value
//otherwise, returns 0
int findUnitClause(int** clauses, int num_clauses,int* solution){
    for(int i = 0; i<num_clauses; i++){
        if(clauses[i][1]==0){
            int literal = clauses[i][0];
            if(solution[abs(literal)-1]==0){
                return literal;
            }
        }
    }
    return 0;
}


//checks recursive base cases for dpll
//returns -1 if any case is false
//returns 1 if all cases are true
//returns 0 if cases are not yet set
int dpllChecker(int** clauses, int num_clauses, int* solution){
    int all_set = 1;
    for(int i = 0; i<num_clauses; i++){
        //printf("i: %d\n",i);
        int clause_sat = 0;
        int set_this_round = 1;
        int j = 0;
        int current_literal = clauses[i][0];
        while(current_literal!=0){
            //printf("curr: %d\n",current_literal);
            int current_var = abs(current_literal);
            if(solution[current_var-1]==current_literal){
                clause_sat = 1;
            }
            else if(solution[current_var-1]==0){
                all_set = 0;
                set_this_round = 0;
            }
            j++;
            current_literal = clauses[i][j];
        }
        if(!clause_sat&&set_this_round){
            return -1;
        }
    }
    if(!all_set){
        return 0;
    }
    return 1;
}

//sets all the values of new_solution with the values if solution
//sets new_val in new_solution
//for recursion in dpll
void newSolution(int* solution, int len_solution, int new_val, int* new_solution){
    //printSolution(solution,len_solution);
    //printf("new solution %d\n",new_val);
    for(int i = 0; i<len_solution;i++){
        //printSolution(new_solution,len_solution);
        if(i!=(abs(new_val)-1)){
            new_solution[i] = solution[i];
        }
        else{
            new_solution[i] = new_val;
        }
    }
    //printSolution(new_solution,len_solution);
    //printf("end of new\n");
}

void printSolution(int* solution, int len_sol){
    for(int i = 0; i<len_sol;i++){
        printf("%d ",solution[i]);
    }
    printf("\n");
}

int localSAT(int** clauses, int num_clauses, int max_walk, int num_symbols){
    int* solution = malloc(num_symbols*sizeof(int));
    int num_false;
    if(solution==NULL){
        printf("error allocating solution");
        exit(1);
    }
    for(int i = 1; i<=num_symbols;i++){
        solution[i-1] = i;
    }
    //printSolution(solution,num_symbols);
    for(int i =0; i<max_walk;i++){
        //printSolution(solution,num_symbols);
        int* false_clause_arr = malloc(num_symbols*sizeof(int));
        num_false = falseRules(clauses,num_clauses,solution,false_clause_arr);
        if(num_false==0){
            printSolution(solution,num_symbols);
            free(solution);
            return num_symbols;
        }
        int best_sat = 0;
        int best_clause = 0;
        int* new_sol = malloc(num_symbols*sizeof(int));
        newSolution(solution,num_symbols,0,new_sol);
        for(int i = 0;i<num_false;i++){
            int sat = maxSat(clauses,num_clauses,new_sol,false_clause_arr[i]);
            if(sat>best_sat){
                best_sat = sat;
                best_clause = i;
            }
            newSolution(solution,num_symbols,0,new_sol);
        }
        int chosen_clause = false_clause_arr[best_clause];
        free(false_clause_arr);
        maxSat(clauses,num_clauses,solution,chosen_clause);
        //printSolution(solution,num_symbols);
    }
    //printSolution(solution,num_symbols);
    free(solution);
    return num_symbols-num_false;
}