from os import path
from handle_intro.services.base_service import BaseService
from handle_intro.utils.helpers import get_attr, generate_id, set_attr
from handle_intro.utils.json import  from_json
from handle_intro.utils.file import read_binary_file
from handle_intro.utils.video import get_video_duration
from handle_intro.models.page import Sentence
from handle_intro.models.intro import Intro


class HandleIntroService(BaseService):

            
    def replace_placeholders(self, text):
        new_text = text
        channel_name = get_attr(self.channel_info, 'name', '')
        new_text = str(new_text).replace("{{channel_name}}", f"{channel_name}")  
        return new_text   
    

    
    def get_service(self, external_services, type):
        services = list(filter(lambda service: service['type'] == type, external_services))
        if (len(services) == 0):
            raise Exception('external service of type ' + type + ' must be injected to the main service' )
        else:
            return services[0]['instance']    

    def __init__(self, config, executer, downloader, saver, external_services = []):

        self.config = config

        self.channel_info = get_attr(self.config, "channel_info", {})

        self.use_subtitles = get_attr(self.channel_info,  'use_subtitles', True)
        self.use_narration = get_attr(self.channel_info,  'use_narration', True)
        self.intro_muted = get_attr(self.channel_info,  'intro_muted', False)

        self.text = get_attr(self.config,  'text', '')

        #workers
        self.executer = executer
        self.downloader = downloader
        self.saver = saver

        self.speech_service = self.get_service(external_services, 'speech')
        self.time_service = self.get_service(external_services, 'add-time')
        self.text_utils_service = self.get_service(external_services, 'text-utils')

        self.temp_directory =   get_attr(self.config,  'temp_directory', '/tmp')
        self.ads =   get_attr(self.config,  'ads', [])

    
    def handle_intro(self, file_object):

        file_path = file_object['file']

        video_time = get_video_duration(file_path)

        #add sentence
        sentences = []
        if (len(str(self.text)) > 0):
            text = self.replace_placeholders(self.text)                
            sentence = Sentence(media_id = None, id = generate_id(),text=text,
                                keywords=None,subtitles=None,speech=None,time=video_time)
        

        #add keywords to sentence
        keywords = self.text_utils_service.extract_keywords(sentence)
        sentence.keywords = keywords

        #add subtitles to sentence
        if (self.use_subtitles == True ):
            subtitles = self.text_utils_service.generate_subtitles_for_sentence(sentence)
            sentence.subtitles = subtitles

        #add speech to sentence
        if ((self.use_narration == True )  and (self.intro_muted == False) ): 
            speech = self.speech_service.get_speech_for_sentence(sentence)
            sentence.speech = speech

        #temporary - for quick test    
        #sentence.speech = from_json('./model.json')


        #download files from s3/mongo when necessary
        binary_files = []
        download_required, downloaded_files = self.download_speech_files(sentence)
        if (download_required):
            
            #change the path of the file
            set_attr(sentence.speech, 'file', downloaded_files[0] )
            binary_files = self.read_binary_files(downloaded_files)

            #add times to sentence
            sentence =  self.time_service.get_time_to_sentence(sentence, binary_files[0])

        else:
            #add times to sentence
            sentence =  self.time_service.get_time_to_sentence(sentence)
 
        sentences.append(sentence)
        intro =  Intro(media_id = generate_id(), path = file_path, path_converted = '', video_time = video_time, sentences = sentences)
        return intro     

    def read_binary_files(self, files):
        binary_downloaded_files = []
        for file in files:
            binary_downloaded_files.append(read_binary_file(file))
        return binary_downloaded_files

    def download_speech_files(self, sentence):
        download_required = False
        downloaded_files = []
        

        #if speech exists and file is remote, download it before:
        speech = get_attr(sentence, 'speech', {})
        if (speech != None):
            source = get_attr(speech, 'source', {})
            if (source != None):
                source_bucket = get_attr(source, 'bucket_name',None)
                if (source_bucket != None): 
                    directory = path.dirname(source['file_path'])
                    file = source['file_id']
                    download_source = {'source_bucket' : source_bucket, "sources": [{ "directory": directory, "objects": [file] }]}
                    self.downloader.reset_sources()
                    self.downloader.add_sources(download_source)
                    download_results, downloaded_files = self.downloader.run()
                    download_required = True
                    if (len(downloaded_files) == 0):
                        raise Exception('download is required,but could not download files from s3 bucket')
                  

                else:
                    download_required = False
                    downloaded_files = [] 
            else:
                download_required = False
                downloaded_files = [] 

        else:
            download_required = False
            downloaded_files = []

        return (download_required, downloaded_files)      

    def execute(self):


        downloaded_files = []
        download_results = []
        result = None
        
        
        #download files
        download_results, downloaded_files = self.downloader.run()

        #save files into target files (for a specific project, for example)
        saved_files = self.saver.run(downloaded_files)     
        
        #convert files to thumbs
        for file in saved_files:
            result  = self.handle_intro(file)

        
        return result

        
       
      