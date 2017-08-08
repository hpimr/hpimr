:appendix-caption: Додаток
:caution-caption: Обережно
:example-caption: Приклад
:figure-caption: Зображення
:important-caption: Важливо
:last-update-label: Востаннє оновлено
//:listing-caption: Лістинг
:manname-title: НАЗВА
:note-caption: Зауваження
//:preface-title: Передмова
:table-caption: Таблиця
:tip-caption: Підказка
:toc-title: Зміст
:untitled-label: Без назви
:version-label: Версія
:warning-caption: Попередження
:apos: &#700;
:lsquo: &laquo;
:rsquo: &raquo;
:ldquo: &bdquo;
:rdquo: &#8223;
${vars}

++++
<script src="./script.js" type="text/javascript"></script>
<link rel="stylesheet" href="./jquery-ui.css">
<div id="access">
<div class="menu-main-menu-container"><ul id="menu-main-menu" class="menu"><li id="menu-item-53" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-home menu-item-53"><a href="/">Зміст</a></li>
<li id="menu-item-101" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-101"><a href="http://hpmor.com/">Оригінал англійською</a></li>
<li id="menu-item-83" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-83"><a href="http://github.com/hpimr/hpimr">github</a></li>
<li id="menu-item-48" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-48"><a href="/help.html">Як долучитися</a></li>
<li id="menu-item-48" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-49"><a href="https://www.facebook.com/groups/212447182535471/">Фейсбук</a></li>
</ul></div>
</div>
<div id="invertable">
<div id="nav-top">${navi}</div>
<div id="storycontent">
++++

include::${currentChapter}.asc[]

++++
</div>
</div>
</div>

<div id="nav-bottom">
<div id="help-with-errors">Помітили помилку? Допоможіть &#8212; виділіть її й натисніть на кнопку &#8220;Помилка?&#8221;. Дякуємо :)</div>
${navi}
</div>
</div>

<div>
<div>
<div style="display:none" id="dialog-message"></div>
<div style="display:none" id="dialog-form" title="Повідомити про помилку">
  <p class="validateTips">Всі поля необовʼязкові.</p>

  <form>
      <input type="hidden" name="fulltext" id="fulltext" value="">
      <input type="hidden" name="translation" id="translation" value="">
      <input type="hidden" name="page" id="page" value="${currentChapter}">
      <table width="100%">
      <tr>
          <td colspan="2"><label for="problem">Що не так:</label></td>
      </tr>
      <tr>
          <td width="100%" colspan="2">
              <textarea rows="3" style="width: 100%" name="problem" id="problem" class="text ui-widget-content ui-corner-all"></textarea>
          </td>
      </tr>
      <tr>
        <td><label for="email">Поштова скринька:</label></td>
        <td><input type="text" name="email" id="email" value="" class="text ui-widget-content ui-corner-all"></td>
      </tr>
      <tr>
        <td><label for="name">Імʼя:</label></td>
        <td><input type="text" name="name" id="name" value="" class="text ui-widget-content ui-corner-all"></td>
      </tr>
      <tr>
        <td><label for="remember">Запамʼятати</label></td>
        <td><input type="checkbox" name="remember" id="remember" value="1" class="ui-widget-content"></td>
      </tr>
      </table>

      <!-- Allow form submission with keyboard without duplicating the dialog button -->
      <input type="submit" tabindex="-1" style="position:absolute; top:-1000px">
  </form>
</div>
<button id="report_error_button">Помилка?</button>
<script src="./google-analytics.js" type="text/javascript"></script>
++++
