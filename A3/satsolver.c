#include <stdio.h>
#include <stdlib.h>
#include <time.h>


//takes the name of the file containing the DIMACS standard SAT info
//reads all info from the file and returns an array of the rules, each rule on one line
int** readfile(char* file_name);

//takes the SAT rules, the probability of a random walk, and the maximum number of changes
//performs walkSAT
//returns true if the SAT problem is satisfied in the given number of changes, false otherwise
//returns the solution/current assignment in solution
int walkSAT(int** clauses, int num_clauses, int p, int max_walk, int* solution, int num_symbols);

//takes all SAT clauses and the current assignment
//returns the number of false clauses
//returns the indices of all false clauses in false_clauses
int falseRules(int** clauses, int num_clauses, int* assignment, int len_assignment, int* false_clauses);

//takes all SAT clauses, the current assignment, and the clause to inspect
//checks all flips of variables in clause to see which gives the most satisfied clauses
//edits assignment to flip that variable
void maxSat(int** clauses, int num_clauses, int* assignment, int len_assignment, int clause);

//takes the SAT rules and symbols
//calls the recursive dpll function
//returns true if saisfiable, false otherwise
//returns the solution/current assignment in solution
int dpllSAT(int** clauses, int num_clauses, int* symbols, int num_symbols, int* solution);

//performs one step of dpll, returns true if satisfiable and the solution in solution
//recursive
//bases cases: every rule is satisfied, one rule is false
//recursions: pure symbol, unit clause, or assign the next symbol
int dpll(int** clauses, int num_clauses, int* symbols, int num_symbols, int* solution, int len_solution);

//takes the SAT rules and symbols and the current assignment
//if a variable only occurs in one value unsolved clauses, returns that value
//otherwise, returns 0
int findPureSymbol(int** clauses, int num_clauses, int* symbols, int num_symbols, int* solution, int len_solution);

//takes the SAT rules and symbols and the current assignment
//if a variable occurs in a unit clause, returns that value
//otherwise, returns 0
int findUnitClause(int** clauses, int num_clauses, int* symbols, int num_symbols, int* solution, int len_solution);



int main(){
    srand(time(NULL));

    return 0;
}

//takes the name of the file containing the DIMACS standard SAT info
//reads all info from the file and returns an array of the rules, each rule on one line
int** readfile(char* file_name){
    FILE *file = fopen(file_name,"r");
    if(file == NULL){
        printf("error opening file");
        exit(1);
    }
    int num_rules, num_vars;
    fscanf(file,"p cnf %d %d\n",num_vars,num_rules);
    int **rules = malloc(num_rules*sizeof(int*));
    if(rules==NULL){
        printf("error allocating rules");
        exit(1);
    }
    for(int i = 0; i<num_rules;i++){
        rules[i] = malloc((num_vars+1)*sizeof(int));
        if(rules[i]==NULL){
            printf("error allocating rules");
            exit(1);
        }
    }
    for(int i = 0;i<num_rules;i++){
        int buffer;
        int j = 0;
        do{
            fscanf(file,"%d",buffer);
            rules[i][j] = buffer;
            j++;
        } while(buffer!=0);
    }
    return rules;
}

//takes the SAT rules, the probability of a random walk, and the maximum number of changes
//performs walkSAT
//returns true if the SAT problem is satisfied in the given number of changes, false otherwise
//returns the solution/current assignment in solution
int walkSAT(int** clauses, int num_clauses, int p, int max_walk, int* solution, int num_symbols){
    solution = malloc(num_symbols*sizeof(int));
    if(solution==NULL){
        printf("error allocating solution");
        exit(1);
    }
    for(int i = 1; i<=num_symbols;i++){
        int positive = rand()%2;
        if(positive){

        }
    }
    return 0;
}

//takes all SAT clauses and the current assignment
//returns the number of false clauses
//returns the indices of all false clauses in false_clauses
int falseRules(int** clauses, int num_clauses, int* assignment, int* false_clauses){
    int num_false = 0;
    int j = 0;
    false_clauses = malloc(num_clauses*sizeof(int));
    if(false_clauses==NULL){
        printf("error allocating false clauses ");
        exit(1);
    }
    for(int i = 0; i<num_clauses; i++){
        int clause_sat = 0;
        int current_literal = clauses[i][0];
        while(!clause_sat && current_literal!=0){
            current_literal = clauses[i][j];
            int current_var = abs(current_literal);
            if(assignment[current_var-1]==current_literal){
                clause_sat = 1;
            }
        }
        if(!clause_sat){
            false_clauses[num_false]=i;
            num_false++;
        }
        j++;
    }
    return num_false;
}

//takes all SAT clauses, the current assignment, and the clause to inspect
//checks all flips of variables in clause to see which gives the most satisfied clauses
//edits assignment to flip that variable
void maxSat(int** clauses, int num_clauses, int* assignment, int fix_clause){
    int *chosen = clauses[fix_clause];
    int best_flip = 0;
    int best_sat = 0;
    int i = 0;
    while(chosen[i]!=0){
        int var = abs(chosen[i]);
        int reset = assignment[var-1];
        int flip;
        if(chosen[i]<0){
            int flip = var;
        }
        else{
            int flip = -var;
        }
        assignment[var-1] = flip;
        int *false_clauses;
        int num_false = falseRules(clauses,num_clauses,assignment,false_clauses);
        int num_true = num_clauses-num_false;
        if(num_true>best_sat){
            best_sat = num_true;
            best_flip = flip;
        }
        assignment[var-1]=reset;
        i++;
    }
    assignment[abs(best_flip)-1] = best_flip;
}

//takes the SAT rules and symbols
//calls the recursive dpll function
//returns true if saisfiable, false otherwise
//returns the solution/current assignment in solution
int dpllSAT(int** clauses, int num_clauses, int* symbols, int num_symbols, int* solution);

//performs one step of dpll, returns true if satisfiable and the solution in solution
//recursive
//bases cases: every rule is satisfied, one rule is false
//recursions: pure symbol, unit clause, or assign the next symbol
int dpll(int** clauses, int num_clauses, int* symbols, int num_symbols, int* solution, int len_solution);

//takes the SAT rules and symbols and the current assignment
//if a variable only occurs in one value in unsolved clauses, returns that value
//otherwise, returns 0
int findPureSymbol(int** clauses, int num_clauses, int* symbols, int num_symbols, int* solution, int len_solution);

//takes the SAT rules and symbols and the current assignment
//if a variable occurs in a unit clause, returns that value
//otherwise, returns 0
int findUnitClause(int** clauses, int num_clauses, int* symbols, int num_symbols, int* solution, int len_solution);


