import sys

class GenerateAst:
    

    def main(self):
        print(sys.argv)
        if sys.argv != 1:
            print("Usage: generate_ast <output directory>")

        outputDir = sys.argv[0]

        self.defineAst(outputDir, "Expr", ["Binary   : Expr left, Token operator, Expr right",
      "Grouping : Expr expression",
      "Literal  : Object value",
      "Unary    : Token operator, Expr right"])


    
    def defineAst(self,outputDir, baseName, types):
        path = outputDir + "/" + baseName + ".py"
        writer = open(path, "x")