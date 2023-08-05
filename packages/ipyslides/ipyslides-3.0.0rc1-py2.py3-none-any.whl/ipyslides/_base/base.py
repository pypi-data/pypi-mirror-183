"Inherit Slides class from here. It adds useful attributes and methods."
import os, re, textwrap
from .widgets import Widgets
from .screenshot import ScreenShot
from .navigation import Navigation
from .settings import LayoutSettings
from .notes import Notes
from .export_html import _HhtmlExporter
from .intro import key_combs
class BaseSlides:
    def __init__(self):
        self.__widgets = Widgets()
        self.__screenshot = ScreenShot(self.__widgets)
        self.clipboard_image = self.__screenshot.clipboard_image # For easy access
        self.__navigation = Navigation(self.__widgets) # Not accessed later, just for actions
        self.__settings = LayoutSettings(self, self.__widgets)
        self.__export = _HhtmlExporter(self)
        self.__notes = Notes(self, self.__widgets) # Needs main class for access to notes
        
        self.toast_html = self.widgets.htmls.toast
        
        self.widgets.checks.toast.observe(self.__toggle_notify,names=['value'])
    
    @property
    def notes(self):
        return self.__notes
    
    @property
    def widgets(self):
        return self.__widgets
    
    @property
    def export(self):
        return self.__export
    
    @property
    def screenshot(self):
        return self.__screenshot
    
    @property
    def settings(self):
        return self.__settings
    
    def notify(self,content,title='IPySlides Notification',timeout=5):
        "Send inside notifications for user to know whats happened on some button click. Set `title = None` if need only content. Remain invisible in screenshot."
        return self.widgets._push_toast(content,title=title,timeout=timeout)
    
    def __toggle_notify(self,change):
        "Blocks notifications if check is not enabled."
        if self.widgets.checks.toast.value:
            self.toast_html.layout.visibility = 'visible' 
            self.notify('Notifications are enabled now!')
        else:
            self.toast_html.layout.visibility = 'hidden'
    
    @property
    def css_styles(self):
        """CSS styles for write(..., className = style)."""
        # self.html will be added from Chid class
        return self.raw('''
        Use any or combinations of these styles in className argument of writing functions:
        ------------------------------------------------------------------------------------
         className          | Formatting Style                                              
        ====================================================================================
         'align-center'     | ------Text------
         'align-left'       | Text------------
         'align-right'      | ------------Text
         'rtl'              | ------ اردو عربی 
         'info'             | Blue Text
         'warning'          | Orange Text
         'success'          | Green Text
         'error'            | Red Text
         'note'             | Text with info icon
         'slides-only'      | Text will not appear in exported html report.
         'report-only'      | Text will not appear on slides. Use to fill content in report.
         'export-only'      | Hidden on main slides, but will appear in exported slides/report.
         'page-break'       | Report will break page in print after object with this class.
         'block'            | Block of text/objects
         'block-[color]'    | Block of text/objects with specific background color from red,
                            | green, blue, yellow, cyan, magenta and gray.
         'raw-text'         | Text will not be formatted and will be shown as it is.
         'zoom-self'        | Zooms object on hover, when Zoom is enabled.
         'zoom-child'       | Zooms child object on hover, when Zoom is enabled.
         'no-zoom'          | Disables zoom on object when it is child of 'zoom-child'.
        ------------------------------------------------------------------------------------
        ''')
        
    def get_source(self, title = 'Source Code'):
        "Return source code of all slides created using `from_markdown` or `%%slide`."
        sources = []
        for slide in self[:]:
            if slide._from_cell and slide._cell_code:
                sources.append(slide._get_source(name=f'Python: Slide {slide.label}'))
            elif slide._markdown:
                sources.append(slide._get_source(name=f'Markdown: Slide {slide.label}'))
        
        if sources:
            return self.keep_format(f'<h2>{title}</h2>' + '\n'.join(s.value for s in sources))
        else:
            self.html('p', 'No source code found.', className='info')

    
    def notify_later(self, title='IPySlides Notification', timeout=5):
        """Decorator to push notification at slide under which it is run. 
        It should return a string that will be content of notifictaion.
        The content is dynamically generated by underlying function, 
        so you can set timer as well. Remains invisible in screenshot through app itself.
        ```python
        @notify_at(title='Notification Title', timeout=5)
        def push_notification():
            time = datetime.now()
            return f'Notification at {time}'
        ```
        """
        if not self._running_slide:
            raise RuntimeError('You can only use this decorator inside a slide constructor.')
        
        def _notify(func): 
            self._running_slide._toast = dict(func = func, kwargs = dict(title=title, timeout=timeout))
        return _notify
        
    def clear_toasts(self):
        "Remove all toast notifications that show up with any slide."
        for s in self._slides_dict.values():
            s._toast = None # remove toast from slide
    
    @property
    def toasts(self):
        "Get all toast notifications attached to slides."
        return tuple([{'slide_key': s.label, 'slide_index': s._index, 'slide_toast': s.toast} for s in self._slides_dict.values() if s.toast])
    
    def _display_toast(self):
        toast = self.current.toast 
        if toast and self.widgets.checks.toast.value: # Only show if toast is enabled, others notification from actions should still be there
            # clear previous content of notification as new one is about to be shown, this will ensure not to see on wrong slide
            self.widgets.htmls.toast.value = ''
            self.notify(content = toast['func'](), **toast['kwargs'])
        
    def from_markdown(self, start, file_or_str, trusted = False):
        """You can create slides from a markdown file or tex block as well. It creates slides `start + (0,1,2,3...)` in order.
        You should add more slides by higher number than the number of slides in the file/text, or it will overwrite.
        Slides separator should be --- (three dashes) in start of line.
        Frames separator should be -- (two dashes) in start of line. All markdown before first `--` will be written on all frames.
        **Markdown Content**
        ```markdown
        # Talk Title
        ---
        # Slide 1 
        || Inline - Column A || Inline - Column B ||
        {{some_var}} that will be replaced by it's html value.
         ```python run source
         myslides = get_slides_instance() # Access slides instance under python code block in markdown
         # code here will be executed and it's output will be shown in slide.
         ```
         {{source}} from above code block will be replaced by it's html value.
        ---
        # Slide 2
        --
        ## First Frame
         ```multicol 40 60
        # Block column 1
        +++
        # Block column 2
        || Mini - Column A || Mini - Column B ||
         ```
        --
        ## Second Frame
        ```
        This will create two slides along with title page if start = 0. Second slide will have two frames.
        
        Markdown content of each slide is stored as .markdown attribute to slide. You can append content to it like this:
        ```python
        with slides.slide(2):
            self.parse_xmd(slides[2].markdown) # Instead of write, parse_xmd take cares of code blocks
            plot_something()
            write_something()
        ```
        Starting from version 1.6.2, only those slides will be updated whose content is changed from last run of this function. This increases speed.
        
        **New in 1.7.2**:     
        - You can add slides from text blocks/file with a start number. 
        - It will create slides at numbers `start, start + 1, .... start + N+1` if there are `N` `---` (three dashes) separators in the text.
        - Find special syntax to be used in markdown by `Slides.xmd_syntax`.
        
        **Returns**:       
        A tuple of handles to slides created. These handles can be used to access slides and set properties on them.
        """
        if self.shell is None or self.shell.__class__.__name__ == 'TerminalInteractiveShell':
            raise Exception('Python/IPython REPL cannot show slides. Use IPython notebook instead.')
        
        if not isinstance(file_or_str, str): #check path later or it will throw error
            raise ValueError(f"file_or_str expects a makrdown file path(str) or text block, got {file_or_str!r}")
        
        if not trusted:
            try: # Try becuase long string will through error for path
                os.path.isfile(file_or_str) # check if file exists then check code blocks
                with open(file_or_str, 'r') as f:
                    lines = f.readlines()
            except:
                lines = file_or_str.splitlines()
                    
            untrusted_lines = []
            for i, line in enumerate(lines, start = 1):
                if re.match(r'```python\s+run', line):
                    untrusted_lines.append(i)
            
            if untrusted_lines:
                raise Exception(f'Given file/text may contain unsafe code to be executed at lines: {untrusted_lines}'
                    ' Verify code is safe and try again with argument `trusted = True`.'
                    ' Never run files that you did not create yourself or not verified by you.')
        
        try:
            if os.path.isfile(file_or_str):
                with open(file_or_str, 'r') as f:
                    chunks = _parse_markdown_text(f.read())
            elif file_or_str.endswith('.md'): # File but does not exits
                raise FileNotFoundError(f'File {file_or_str} does not exist.')
            else:
                chunks = _parse_markdown_text(file_or_str)
        except:
            chunks = _parse_markdown_text(file_or_str)
            
        handles = self.create(*range(start, start + len(chunks))) # create slides faster
        
        for i,chunk in enumerate(chunks, start = start):
            # Must run under this to create frames with two dashes (--)
            self.shell.run_cell_magic('slide', f'{i} -m', chunk)
        
        # Return refrence to slides for quick update, frames should be accessed by slide.frames
        return handles
    
    def demo(self):
        "Demo slides with a variety of content."
        from .. import _demo
        return _demo.demo(self) # Run demo
        
    def docs(self):
        "Create presentation from docs of IPySlides."
        self.close_view() # Close any previous view to speed up loading 10x faster on average
        self.clear() # Clear previous content
        self.create(*range(13)) # Create slides faster
        
        from ..core import Slides
        self.settings.set_footer('IPySlides Documentation')
        
        auto = self.AutoSlides() # Does not work inside notebook (should not as well)
        
        with auto.title(): # Title
            self.write(f'## IPySlides {self.version} Documentation\n### Creating slides with IPySlides')
            self.center('''
                alert`Abdul Saboor`sup`1`, Unknown Authorsup`2`
                section`Introduction`
                today``
                
                ::: text-box
                    sup`1`My University is somewhere in the middle of nowhere
                    sup`2`Their University is somewhere in the middle of nowhere
                ''').display()
        
        with auto.slide() as slide_toc1: # Need at end to refresh TOC
            self.write('## Table of Contents')
            
        with auto.slide():
            self.write(['# Main App',self.doc(Slides)])
        
        with auto.slide():
            self.write('## Adding Slides section`Adding Slides and Content`')
            self.write('Besides functions below, you can add slides with `%%title` magics as well.\n{.note .info}')
            self.write([self.doc(self.title,'Slides'),self.doc(auto.slide,'Slides'),self.doc(self.frames,'Slides'),self.doc(self.from_markdown,'Slides')])
        
        with auto.slide():
            self.write('## Adding Content')
            self.write('Besides functions below, you can add content to slides with `%%xmd`,`%xmd`, `display(obj)` as well.\n{.note .info}')
            self.xmd_syntax.display() # This will display information about Markdown extended syntax
            self.write([self.doc(self.write,'Slides'),self.doc(self.iwrite,'Slides'), self.doc(self.parse_xmd,'Slides'),self.doc(self.cite,'Slides')])
        
        with auto.slide():
            self.write('## Adding Speaker Notes')
            self.write([f'You can use alert`notes\`notes content\`` in markdown.\n{{.note .success}}\n',
                       'This is experimental feature, and may not work as expected.\n{.block-red .error}'])
            self.doc(self.notes,'Slides.notes', members = True, itself = False).display()
            self.goto_button(10,'Jump to Slide 10', 'This is kind a alert`alt text` because button will alert`NOT` show in screenshot of slides')
                   
        with auto.slide():
            self.write('## Displaying Source Code')
            self.doc(self.source,'Slides.source', members = True, itself = False).display()
        
        with auto.slide()  as slide_toc2: # Need at end to refresh TOC
            self.write('## Table of Contents section`?Layout and color[yellow_black]`Theme` Settings?`')
        
        with auto.slide(): 
            self.write('## Layout and Theme Settings')
            self.doc(self.settings,'Slides.settings', members=True,itself = False).display()
                
        with auto.slide():
            self.write('## Useful Functions for Rich Content section`?Useful Functions for alert`Rich Content`?`')
            members = ['alert','block', 'bokeh2html', 'bullets','cite',
                       'colored', 'cols', 'details', 'doc','sub','sup', 'today', 'enable_zoom', 'format_css', 'format_html', 'highlight',
                       'html', 'iframe', 'image', 'keep_format', 'notify', 'notify_later', 'plt2html', 'raw', 'rows',
                        'section', 'set_dir', 'sig', 'textbox', 'suppress_output','suppress_stdout','svg', 'vspace']
            self.doc(self.clipboard_image,'Slides').display()
            self.doc(self, 'Slides', members = members, itself = False).display()
            
        with auto.slide():
            self.write('## Content Styling')
            with self.source.context(auto_display = False) as c:
                self.write(('You can **style**{.error} or **color[teal]`colorize`** your *content*{: style="color:hotpink;"} and *color[hotpink_yellow]`text`* with `className` attribute in writing/content functions. ' 
                       'Provide **CSS**{.info} for that using `.format_css` or use some of the available styles. '
                       'See these **styles**{.success} with `.css_styles` property as below:'))
                self.css_styles.display()
                c.display()
        
        s8, = auto.from_markdown('''
        ## Highlighting Code
        [pyg]:`[pygments](https://pygments.org/) is used for syntax highlighting.`
        You can **highlight**{.error} code using `highlight` function or within markdown like this:cite`pyg`
        ```python
        import ipyslides as isd
        ```
        ```javascript
        import React, { Component } from "react";
        ```
        ''', trusted= True)
        
        # Update with source of slide
        with s8.insert(-1): # Insert source code
            self.write('<hr/>This slide was created with `from_markdown` function. '
                'So its source code can be inserted in the slide later! '
                'See at last slide how it was done!<hr/>')
            self.write(s8.citations)
            s8.source.display()
        
        with auto.slide():
            self.write('## Loading from File/Exporting to HTML section`Loading from File/Exporting to HTML`')
            self.write('You can parse and view a markdown file w. The output you can save by exporting notebook in other formats.\n{.note .info}')
            self.write([self.doc(self.from_markdown,'Slides'),
                        self.doc(self.demo,'Slides'), 
                        self.doc(self.docs,'Slides'),
                        self.doc(self.export.slides,'Slides.export'),
                        self.doc(self.export.report,'Slides.export')])
        
        with auto.slide() as slide_toc3: # Need at end to refresh TOC
            self.write('## Table of Contents section`Advanced Functionality`')
        
        with auto.slide():
            self.write('## Adding User defined Objects/Markdown Extensions')
            self.write('If you need to serialize your own or third party objects not serialized by this module, you can use `@Slides.serializer.register` to serialize them to html.\n{.note .info}')
            self.doc(self.serializer,'Slides.serializer', members = True, itself = False).display()
            self.write('**You can also extend markdown syntax** using `markdown extensions`, ([See here](https://python-markdown.github.io/extensions/) and others to install, then use as below):')
            self.doc(self.extender,'Slides.extender', members = True, itself = False).display()
        
        with auto.slide():
            self.write('## Keys and Shortcuts\n'
                '- You can use `Slides.current` to access a slide currently in view.\n'
                '- You can use `Slides.running` to access the slide currently being built,'
                ' so you can set CSS, aminations etc.', key_combs)
        
        with auto.slide():
            self.write('''
            ## Focus on what matters
            - There is a zoom button on top bar which enables zooming of certain elements. This can be toggled by `Z` key.
            - Most of supported elements are zoomable by default like images, matplotlib, bokeh, PIL image, altair plotly, dataframe, etc.
            - You can also enable zooming for an object/widget by wrapping it inside `Slide.enable_zoom` function conveniently.
            - You can also enable by manully adding `zoom-self`, `zoom-child` classes to an element. To prevent zooming under as `zoom-child` class, use `no-zoom` class.
            
            ::: zoom-self block-red
                ### Focus on Me 😎
                - If zoom button is enabled, you can hover here to zoom in this part!
                - You can also zoom in this part by pressing `Z` key while mouse is over this part.
            ''')
        with auto.slide():
            self.write('''
                ## SVG Icons
                Icons that apprear on buttons inslides (and their rotations) available to use in your slides as well.
                ''')
            self.write(' '.join([f'`{k}`: ' + self.icon(k,color='crimson').svg for k in self.icon.available]))
            
            with self.source.context():
                import ipywidgets as ipw
                btn = ipw.Button(description='Chevron-Down',icon='plus').add_class('MyIcon') # Any free font awesome icon, but class is important to overwrite icon     
                self.iwrite(btn)
                self.format_css({'.MyIcon .fa.fa-plus': self.icon('chevron',color='crimson', size='1.5em',rotation=90).css}).display() # Overwrite icon with your own

            
        with auto.slide():
            self.write(['# Auto Slide Numbering in Python Scripts', self.doc(self.AutoSlides,'Slides')])
        
        with auto.slide():
            self.write(['## Presentation Code section`Presentation Code`',self.docs])
        
        for slide in [slide_toc1, slide_toc2, slide_toc3]:
            slide.insert_markdown({-1: 'toc`------`'}) # Update table of contents at end
         
        self.navigate_to(0) # Go to title
        return self

def _parse_markdown_text(text_block):
    "Parses a Markdown text block and returns text for title and each slide."
    lines = textwrap.dedent(text_block).splitlines() # Remove overall indentation
    breaks = [-1] # start, will add +1 next
    for i,line in enumerate(lines):
        if line and line.strip() =='---':
            breaks.append(i)
    breaks.append(len(lines)) # Last one
    
    ranges = [range(j+1,k) for j,k in zip(breaks[:-1],breaks[1:])]
    return ['\n'.join(lines[x.start:x.stop]) for x in ranges]
        