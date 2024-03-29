from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from main.views import uploadList, upload, home, authentication, team, email, qna

urlpatterns = [
    path('home/', home.homeView,name='home'),
    path('home/homeInfoJson/', home.homeInfoJson, name='homeInfoJson'),
    path('home/homeBoardJson/', home.homeBoardJson, name='homeBoardJson'),
    path('login/', authentication.loginView, name='login'),
    path('logout/', authentication.logoutView,name='logout'),
    path('join/', authentication.joinView, name='join'),
    path('edit/pwd', authentication.pwdeditView, name='pwdedit'),
    path('edit/id', authentication.ideditView, name='idedit'),
    path('edit/pwdEditJson', authentication.pwdEditJson, name='pwdEditJson'),
    path('edit/idEditJson', authentication.idEditJson, name='idEditJson'),
    path('team/homeTeamJson/', team.homeTeamJson, name='homeTeamJson'),
    path('team/', team.teamView, name='team'),
    path('team/teamJson/', team.teamJson,name='teamJson'),
    path('upload/', upload.uploadView,name='upload'),
    path('uploadList/', uploadList.uploadListView, name='uploadList'),
    path('uploadList/uploadDelete/<id>', uploadList.uploadListDelete, name='uploadDelete'),
    path('uploadList/uploadDownload/<id>', views.uploadList.uploadListDownload, name='uploadDownload'),
    path('email/', email.emailView, name='email'),
    path('qna/qnaList/', qna.qnaListView,name='qnaList'),
    path('qna/qnaWrite/', qna.qnaWriteView,name='qnaWrite'),
    path('qna/qnaReadAndReply/<qnaId>/', qna.qnaReadAndReplyView, name='qnaReadAndReply'),
    path('qna/qnaReplyJson/<qnaId>/', qna.qnaReplyJson, name='qnaReplyJson'),
    path('guide/', views.guideView,name='guide'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


