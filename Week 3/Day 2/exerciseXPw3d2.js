const paragraphs = document.getElementsByTagName('p');
console.log(paragraphs)
for (var i = 0; i < paragraphs.length; i++) {
	paragraphs[i].setAttribute('class','para_article');

}

const myArticle = document.querySelector('article')
myArticle.removeChild(myArticle.lastElementChild)
