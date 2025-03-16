#!/usr/bin/env python

# This is an interpreter for SCREAM programming language, written in Python 3.7.

import sys
import os
import io

import re

GLOBAL_VAR_DICT = {}

GLOBAL_FUNC_DICT = {}

GLOBAL_LET_DICT = {}



def remove_strings(statement):
    """
    A function to remove strings from the statement.
    """
    cleaned_statement = statement
    while "'" in cleaned_statement:
        if cleaned_statement.count("'") % 2 == 0:
            if cleaned_statement.count("'") > 0:
                start = cleaned_statement.find("'")
                end = cleaned_statement.find("'", start + 1)
                cleaned_statement = \
                cleaned_statement[:start] + 'A_STRING_WAS_HERE' + \
                cleaned_statement[end + 1:]
            else:
                break
        else:
            raise ValueError('Uneven count of single quotes.')
    return cleaned_statement

    # TODO: Needed?


def remove_comments(statement):
    """
    A function to remove comments from the statement.
    """
    sanitized_statement = statement
    strings_removed = remove_strings(sanitized_statement)
    if '//' in strings_removed:
        sanitized_statement = \
            sanitized_statement[:sanitized_statement.rfind('//')].strip()
    return sanitized_statement


def usage():
    print("This is an interpreter for the SCREAM programming language.")
    print("Usage:")
    print(f"{sys.argv[0]} scream_program.scream")

def func_handler(command,params,program_io):
    func_name = params
    if re.match(re'[A-Z0-9_]')

def begin(command,program_io):
    while program_io != 'END':
        program_io += 1
        if command == 'LET':
            let_handler()
        elif command == 'PRINT':
            print_handler()
        elif command == 'RETURN':
            


def evaluate_expression(command,expression,program_io):
    var_exp = expression[1:]
    if re.match(r'\*(\([A-Z0-9,A-Z0-9])',var_exp):
        while program_io != 'END':
            begin()
            program_io += 1

def print_handler(command, params, program_io):
    expression = params
    if re.match(r'\w+\s*[\+\*\/\-\%]\s*\w+', expression):
        print(expressions)
    elif re.match(r'[A-Z0-9]'):


def let_handler(command, params, program_io):
    let_name = re.findall(r'[A-Z0-9_]+(\[A-Z0-9])?',params)[0]
    expression = re.split(let_name,params,maxsplit=1)[1].strip()
    if expression.startswith('='):
        value = evaluate_expression(expression[1:])
    elif expression.startswith('('):
        value = evaluate_expression(expression[1:])
    elif re.match(r'\-?\d+(?:\.\d+)?;', expression):
        string_value = re.findall(r'\-?\d+(?:\.\d+)?', expression)[0]
        if '.' in string_value:
            value = float(string_value)
        else:
            value = int(string_value)
    GLOBAL_LET_DICT[let_name] = value


def var_handler(command, params, program_io):
    """

    :param command:
    :type command:
    :param params:
    :type params:
    :return:
    :rtype:
    """
    value = 'NIL'
    variable_name = re.findall(r'[A-Z0-9_]+', params)[0]
    expression = re.split(variable_name, params, maxsplit=1)[1].strip()
    if expression.startswith('='):
        value = evaluate_expression(expression[1:])
    elif re.match(r'\-?\d+(?:\.\d+)?;', expression):
        string_value = re.findall(r'\-?\d+(?:\.\d+)?', expression)[0]
        if '.' in string_value:
            value = float(string_value)
        else:
            value = int(string_value)
    GLOBAL_VAR_DICT[variable_name] = value


keyword_function_mapper = {'VAR': var_handler, 'LET': let_handler}


def main():
    if len(sys.argv) != 2:
        print("Incorrect number of arguments.")
        usage()
        return -1

    filename = sys.argv[1]
    if not os.path.isfile(filename):
        print("Invalid filename provided in the argument. The file does not "
              "exist.")
        return -2

    with open(filename) as fp:
        program_text = fp.read()

    program_size = len(program_text)

    program_io = io.StringIO(program_text)

    # Until the end of program.
    line_number = 0
    while program_io.tell() != program_size:
        line = program_io.readline().strip()
        line_number += 1

        line_without_comments = remove_comments(line)
        tokens = line_without_comments.split(maxsplit=1)
        if len(tokens) > 1:
            command, params = tokens
        else:
            command, params = tokens[0], ''
        if command != 'VAR':
            print(f'Not implemented the handler for {command} yet.')
            print(f"{line_number:3}: {line}")
            continue
        keyword_function_mapper[command](command, params, program_io)

    print(f'GLOBAL_VAR_DICT: {GLOBAL_VAR_DICT}')

    program_io.close()


if __name__ == '__main__':
    sys.exit(main())
