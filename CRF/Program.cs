using CRFSharpWrapper;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CRF_for_NLP
{
    class Program
    {
        static void Main(string[] args)
        {
            var encoder = new CRFSharpWrapper.Encoder();
            var options = new EncoderArgs();
            options.debugLevel = 1;
            options.strTemplateFileName = @"D:\NLP\template.NE"; //template file name  
            options.strTrainingCorpus = @"D:\NLP\fold4_training.txt"; //training corpus file name  
            options.strEncodedModelFileName = @"D:\NLP\ner_model"; //encoded model output file name  
            options.max_iter = 1000;
            options.min_feature_freq = 2;
            options.min_diff = 0.0001;
            options.threads_num = 1;
            options.C = 1.0;
            options.slot_usage_rate_threshold = 0.95;
            bool bRet = encoder.Learn(options);
        }
    }
}
