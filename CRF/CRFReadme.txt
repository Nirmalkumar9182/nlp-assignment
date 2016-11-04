For the purpose of API recognition in our project, a Conditional Random Field implementation in C# known as CRFSharp was used, below is a guide on how to train and test a model using the sample training and testing files provided.

Files and folders included in the CRF folder are as follows:

CRFSharpDemoPackage
- The CRF tool obtained from https://github.com/zhongkaifu/CRFSharp under "Releases", the bin folder contains CRFSharpWrapper.dll, used for encoding(training), and CRFSharpConsole.exe, used for decoding(testing). The other files remain unused. 
This library is included because the file size is extremely small (343 KB)

CRF_for_NLP
- Contains a C# project created in Visual Studio Community 2015. Inside is Program.cs, which is the code for encoding(training) a CRF model.

training.txt
- A sample file used for the encoding(training) process. 
Each line contains one token, then a tab, then the POS tag of the token, then another tab, then the BILOU tag of the token.

testing.txt
- A sample file used for the decoding(testing) process.
Each line contains one token, then a tab, then the POS tag of the token, but no BILOU tag.

template.NE
- The template file used by the CRF tool for feature generation. Each line in the file is an index followed by a rule string. 
The simplest format for rule string is "%x[y,z]", x is a variable that the result will be assigned to, z can be either 0 for the current token or 1 for its POS tag, and y denotes the position relative to the current token.

For example, assuming the current token is "cats" in:

like	VB	O
cats	NNS	O

then %x[0,0] will give "cats", %x[0,1] will give "NNS", and %x[-1,0] will give "like".
The rule strings can be further combined like "%x[-1,1]/%x[0,1]" which will give "VB/NNS"


Encoding:
	1) Open the C# project CRF_for_NLP in Visual Studio, make sure CRFSharpWrapper.dll is already added as a project reference. 
	
	2) Change the string variables "strTemplateFileName" and "strTrainingCorpus" in Program.cs. These contain the file paths that should point to where template.NE and training.txt are located in the system.
	
	3) Also change the string variable "strEncodedModelFileName", this contains the file path where the model files should be outputted to, and also determines the name of the model files ("ner_model" by default).
	
	4) The other parameters can be left as is.
	
	5) Run Program.cs, a command prompt window should open showing that CRFSharp is encoding a model based on training.txt and template.NE
	
	6) After the encoding process is done. 4 model files should be outputted. Assuming the model files are named "ner_model", then these 4 files will be "ner_model", "ner_model.alpha", "ner_model.feature", and "ner_model.feature.raw_text".
	
	7) The encoding process is finished.

Decoding:
	1) Open a command prompt window.
	
	2) Chance the current directory to 'x\CRFSharpDemoPackage\bin'. Where x stands for the file path where this folder is located on the system.
	
	3) Run the command "CRFSharpConsole.exe -decode -modelfile y\ner_model -inputfile y\testing.txt -outputfile y\testing_results.txt". Where y stands for the file path where the model files outputted earlier during encoding, and the testing file, are located.
	
	4) Observe that a new file, "testing_results.txt", has been created in the directory pointed to by y.
	
	5) This concludes the decoding process. Note how the result file now has BILOU tags for every token.


