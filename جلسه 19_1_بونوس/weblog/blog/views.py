from django.urls import reverse, reverse_lazy
from django.views import generic

from .forms import PostForm
from .models import Post

class PostListView(generic.ListView):
    model = Post
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(status='pub').order_by('-datetime_modified')

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    # pk chi mishe? خودش به صورت پیش فرض، اسم pk رو انتخاب میکنه. یعنی اگه توی ویومون اسمش رو چیز دیگه گذاشته بودیم الان باید اسمش رو عوض میکردیم میذاشتیم pk.
    context_object_name = 'post' # اگه ننویسیم هم کار میکنه. خودش پیش فرض اسم مدل رو برمیداره و حروف کوچیکش میکنه و به عنوان کانتکست نیم میده به اچ تی ام ال. جل الخالق :دی

class PostCreateView(generic.CreateView):
    # model = Post اینجا لازم نیست. خودش از روی فرم کلس که نوشتیم و داخلش از پست استفاده کردیم میفهمه که مدلمون پست هست.
    form_class = PostForm
    template_name = 'blog/new_post.html'
    # با این دو تا، اگه ولید باشه پست رو میسازه. ولی نمیدونه به کجا ریدایرکت کنه. اینجا رفتیم تابع گت ابسلوت یو آر ال رو توی ویو نوشتیم.
    # success_url = reverse_lazy('posts_list') # اول کار این رو نذاشته بودم تا درس بده. وقتی این نیست میگرده دنبال گت ابسلوت یو آر ال. اگه نوشته باشیم که اون رو میاره. اگه نه که ارور میده. وقتی این خط رو بذاریم، کلا چون خودمون بهش گفتیم برو اینجا میره اینجا و به گت ابسلوت یو آر ال کاری نداره.

# این مدل بهتر هست نسبت به بعدی. اما بعدی رو نوشتم که بگم لزومی نداره حتما از اتریبیوت فرم کلس استفاده کنیم.
class PostUpdateView(generic.UpdateView):
    model = Post # اینجا ولی لازم هست. چون فرم رو درسته که بهش گفتیم. ولی میخواد با یک سری اطلاعات قبلی این فرم رو پر کنه. اون اطلاعات چی هستند، مدل رو باید بهش بگیم اینجا.
    form_class = PostForm
    template_name = 'blog/new_post.html'
# class PostUpdateView(generic.UpdateView):
#     model = Post # اینجا ولی لازم هست. چون فرم رو درسته که بهش گفتیم. ولی میخواد با یک سری اطلاعات قبلی این فرم رو پر کنه. اون اطلاعات چی هستند، مدل رو باید بهش بگیم اینجا.
#     fields = ['title', 'text', 'author']
#     template_name = 'blog/new_post.html'


class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('posts_list')

    # روش 2 که از ریورس لیزی استفاده نکنه.
    '''
    دلیل مشکل: توابع تا کال نشن، بررسی نمیشن. پس سرور که داره ران میشه بهش گیر نمیده.
    چون توی تابع هست. در حالی که اگه بنویسیسم ساکسس یو آر ال مساوی با ریورس پستس لیست
    همون لحظه میخواد پیداش کنه. ولی خب نمیتونه پیداش کنه و سرکولار ایمپورت رخ میده.
    '''
    # def get_success_url(self):
    #     return reverse('posts_list')
