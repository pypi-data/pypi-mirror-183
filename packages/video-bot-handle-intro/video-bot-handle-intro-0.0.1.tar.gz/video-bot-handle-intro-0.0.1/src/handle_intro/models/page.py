from typing import AnyStr, List

class Author:
     def __init__(self, 
        name: AnyStr = None,
        link: AnyStr = None) -> None:

        self.name = name
        self.link = link

class Meta:
     def __init__(self, 
        description: AnyStr = None,
        duration: AnyStr = None,
        uploadDate: AnyStr = None,):

        self.description = description
        self.duration = duration
        self.uploadDate = uploadDate

class Image:
      def __init__(self, 
        title: AnyStr = None,
        meta: Meta = None,
        source: AnyStr = None,
        alternative_text: AnyStr = None):

        self.title = title
        self.meta = meta
        self.source = source
        self.alternative_text = alternative_text

class Movie:
      def __init__(self, 
        title: AnyStr = None,
        meta: Meta = None,
        source: AnyStr = None):

        self.title = title
        self.meta = meta
        self.source = source


class Section:
     def __init__(self, 
        title: AnyStr = None,
        description: AnyStr  = None,
        paragraphs: List[AnyStr] = None,
        images: List[Image] = None,
        movies: List[Movie] = None,
        section_type: AnyStr = None,
        related_id: AnyStr = None,
        _id: AnyStr = None,
        is_title = None,
        is_ad = None,
        attributes = None
        
        ) -> None:
    
        self.section_type = section_type
        self.id = _id
        self.title = title
        self.description = description,
        self.paragraphs = paragraphs
        self.images = images
        self.movies = movies
        self.attributes = attributes
        self.related_id = related_id
        self.is_ad = is_ad
        self.is_title = is_title
        

class Page:
    def __init__(self, 
     title = None,
     category = None,
     sections: List[Section] = None,
     summary: List[AnyStr] = None,
     authors: Author = None,
     publish_date: AnyStr = None,
     images: List[Image] = None,
     movies: List[Movie] = None
    ) -> None:
        
        self.title = title
        self.category = category
        self.sections = sections
        self.summary = summary
        self.authors = authors
        self.publish_date = publish_date
        self.images = images
        self.movies = movies

class Sentence:
     def __init__(self, 
                media_id = None,
                id = None,
                text = None,
                keywords = [],
                subtitles = [], 
                speech = None,
                time = 0) -> None:
        
        self.text = text
        self.keywords = keywords       
        self.subtitles =  subtitles
        self.speech = speech
        self.time = time
        self.media_id = media_id
        self.id = id
        