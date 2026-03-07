import language_tool_python
import autopep8
import sys
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class SyntaxSurgeon:
    def __init__(self):
        print("Initializing The Syntax Surgeon...")
        print("Loading grammar models (this may take a moment)...")
        # Initialize the grammar tool
        self.grammar_tool = language_tool_python.LanguageTool('en-US')
        print("Surgeon is ready for operation.\n")

    def operate_on_text(self, text):
        print("\n--- OPERATION: TEXT REPAIR ---")
        matches = self.grammar_tool.check(text)
        
        if not matches:
            print("Status: Patient is healthy. No syntax errors found.")
            return
        
        print(f"Status: Found {len(matches)} issues. Applying fixes...")
        corrected_text = self.grammar_tool.correct(text)
        print(f"\nResult: {corrected_text}")

    def operate_on_code(self, code_snippet):
        print("\n--- OPERATION: CODE REFACTORING ---")
        try:
            compile(code_snippet, '<string>', 'exec')
            print("Syntax check passed. Formatting code...")
            fixed_code = autopep8.fix_code(code_snippet)
            print("\nResult:\n")
            print(fixed_code)
        except SyntaxError as e:
            print(f"CRITICAL ERROR: {e.msg} at line {e.lineno}")

def main():
    try:
        surgeon = SyntaxSurgeon()
        
        while True:
            print("\n" + "="*30)
            print(" THE SYNTAX SURGEON v1.0 (EXE) ")
            print("="*30)
            print("1. Text Surgery (Fix Grammar)")
            print("2. Code Surgery (Fix Python Formatting)")
            print("3. Exit")
            
            choice = input("\nSelect Option (1-3): ").strip()
            
            if choice == '1':
                text = input("\nEnter text: ")
                surgeon.operate_on_text(text)
                input("\nPress Enter to continue...")
                clear_screen()
                
            elif choice == '2':
                print("\nEnter Python code (type 'END' on a new line to finish):")
                lines = []
                while True:
                    line = input()
                    if line.strip() == 'END':
                        break
                    lines.append(line)
                code = "\n".join(lines)
                surgeon.operate_on_code(code)
                input("\nPress Enter to continue...")
                clear_screen()
                
            elif choice == '3':
                break
                
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        input("Press Enter to close...")

if __name__ == "__main__":
    main()