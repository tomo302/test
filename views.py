from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from crud.models import Member
from crud.forms import MemberForm
from django.views.generic import ListView #追加

#　一覧
def index(request):

    #return HttpResponse("一覧")

    members = Member.objects.all().order_by('id')

    return render(request, 'members/index.html', {'members': members})

#一覧（ページネーション用に追加）
class MemberList(ListView):
    model = Member #利用するモデル
    context_object_name='members' #オブジェクト名の設定（標準ではobject_listとなってしまう）
    template_name='members/index.html' #テンプレートページの指定
    paginate_by = 10 #1ページあたりのページ数

#　新規と編集
def edit(request, id=None):

    if id: #idがあるとき（編集の時）
        #idで検索して、結果を戻すか、404エラー
        member = get_object_or_404(Member, pk=id)
    else: #idが無いとき（新規の時）
        #Memberを作成
        member = Member()

    #POSTの時（新規であれ編集であれ登録ボタンが押されたとき）
    if request.method == 'POST':
        #フォームを生成
        form = MemberForm(request.POST, instance=member)
        if form.is_valid(): #バリデーションがOKなら保存
            member = form.save(commit=False)
            member.save()
            return redirect('crud:index')
    else: #GETの時（フォームを生成）
        form = MemberForm(instance=member)

    #新規・編集画面を表示
    return render(request, 'members/edit.html', dict(form=form, id=id))

def delete(request, id):
    # return HttpResponse("削除")
    member = get_object_or_404(Member, pk=id)
    member.delete()
    return redirect('crud:index')

def detail(request, id=id):
    member = get_object_or_404(Member, pk=id)
    return render(request, 'members/detail.html', {'member':member})