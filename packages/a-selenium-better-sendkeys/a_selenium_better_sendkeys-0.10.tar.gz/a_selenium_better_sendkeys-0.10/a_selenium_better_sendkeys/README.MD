# As reliable as send_keys, but almost as fast as execute_script(arguments[0].value=...)

```python
# Tested with:
# https://github.com/ultrafunkamsterdam/undetected-chromedriver
# Python 3.9.13
# Windows 10

$pip install a-selenium-better-sendkeys

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from a_selenium2df import get_df
from selenium.webdriver.common.by import By
from a_selenium_kill import add_kill_selenium
from time import sleep
from auto_download_undetected_chromedriver import download_undetected_chromedriver
import undetected_chromedriver as uc

from a_selenium_better_sendkeys import send_keys_alternative


@add_kill_selenium  # https://github.com/hansalemaos/a_selenium_kill
def get_driver():
    folderchromedriver = "f:\\seleniumdriver2"
    path = download_undetected_chromedriver(
        folder_path_for_exe=folderchromedriver, undetected=True
    )  # https://github.com/hansalemaos/auto_download_undetected_chromedriver
    driver = uc.Chrome(driver_executable_path=path)
    return driver


if __name__ == "__main__":
    folderchromedriver = "f:\\seleniumdriver3"
    path = download_undetected_chromedriver(
        folder_path_for_exe=folderchromedriver, undetected=True
    )
    driver = get_driver()
    driver.get(r"https://translate.google.com/")
    sleep(2)
    df = get_df(
        driver, By, WebDriverWait, expected_conditions, queryselector="textarea"
    )  # https://github.com/hansalemaos/a_selenium2df

    texts = r"""Blumfeld, ein älterer Junggeselle, stieg eines abends zu seiner Wohnung hinauf, was eine mühselige Arbeit war, denn er wohnte im sechsten Stock. Während des Hinaufsteigens dachte er, wie öfters in der letzten Zeit, daran, daß dieses vollständig einsame Leben recht lästig sei, daß er jetzt diese sechs Stockwerke förmlich im Geheimen hinaufsteigen müsse, um oben in seinen leeren Zimmern anzukommen, dort wieder förmlich im Geheimen den Schlafrock anzuziehn, die Pfeife anzustecken, in der französischen Zeitschrift, die er schon seit Jahren abonniert hatte, ein wenig zu lesen, dazu an einem von ihm selbst bereiteten Kirschenschnaps zu nippen und schließlich nach einer halben Stunde zu Bett zu gehn, nicht ohne vorher das Bettzeug vollständig umordnen zu müssen, das die jeder Belehrung unzugängliche Bedienerin immer nach ihrer Laune hinwarf. Irgendein Begleiter, irgendein Zuschauer für diese Tätigkeiten wäre Blumfeld sehr willkommen gewesen. Er hatte schon überlegt, ob er sich nicht einen kleinen Hund anschaffen solle. Ein solches Tier ist lustig und vor allem dankbar und treu; ein Kollege von Blumfeld hat einen solchen Hund, er schließt sich niemandem an, außer seinem Herrn, und hat er ihn ein paar Augenblicke nicht gesehn, empfängt er ihn gleich mit großem Bellen, womit er offenbar seine Freude darüber ausdrücken will, seinen Herrn, diesen außerordentlichen Wohltäter wieder gefunden zu haben. Allerdings hat ein Hund auch Nachteile. Selbst wenn er noch so reinlich gehalten wird, verunreinigt er das Zimmer. Das ist gar nicht zu vermeiden, man kann ihn nicht jedesmal, ehe man ihn ins Zimmer hineinnimmt, in heißem Wasser baden, auch würde das seine Gesundheit nicht vertragen. Unreinlichkeit in seinem Zimmer aber verträgt wieder Blumfeld nicht, die Reinheit seines Zimmers ist ihm etwas Unentbehrliches, mehrmals in der Woche hat er mit der in diesem Punkte leider nicht sehr peinlichen Bedienerin Streit. Da sie schwerhörig ist, zieht er sie gewöhnlich am Arm zu jenen Stellen des Zimmers, wo er an der Reinlichkeit etwas auszusetzen hat. Durch diese Strenge hat er es erreicht, daß die Ordnung im Zimmer annähernd seinen Wünschen entspricht. Mit der Einführung eines Hundes würde er aber geradezu den bisher so sorgfältig abgewehrten Schmutz freiwillig in sein Zimmer leiten. Flöhe, die ständigen Begleiter der Hunde, würden sich einstellen. Waren aber einmal Flöhe da, dann war auch der Augenblick nicht mehr fern, an dem Blumfeld sein behagliches Zimmer dem Hund überlassen und ein anderes Zimmer suchen würde. Unreinlichkeit war aber nur ein Nachteil der Hunde. Hunde werden auch krank und Hundekrankheiten versteht doch eigentlich niemand. Dann hockt dieses Tier in einem Winkel oder hinkt herum, winselt, hüstelt, würgt an irgendeinem Schmerz, man umwickelt es mit einer Decke, pfeift ihm etwas vor, schiebt ihm Milch hin, kurz, pflegt es in der Hoffnung, daß es sich, wie es ja auch möglich ist, um ein vorübergehendes Leiden handelt, indessen aber kann es eine ernsthafte, widerliche und ansteckende Krankheit sein. Und selbst wenn der Hund gesund bleibt, so wird er doch später einmal alt, man hat sich nicht entschließen können, das treue Tier rechtzeitig wegzugeben, und es kommt dann die Zeit, wo einen das eigene Alter aus den tränenden Hundeaugen anschaut. Dann muß man sich aber mit dem halbblinden, lungenschwachen, vor Fett fast unbeweglichen Tier quälen und damit die Freuden, die der Hund früher gemacht hat, teuer bezahlen. So gern Blumfeld einen Hund jetzt hätte, so will er doch lieber noch dreißig Jahre allein die Treppe hinaufsteigen, statt später von einem solchen alten Hund belästigt zu werden, der, noch lauter seufzend als er selbst, sich neben ihm von Stufe zu Stufe hinaufschleppt. """
    send_keys_alternative(driver, df.element.iloc[0], texts[:4000])
    
    
	
```




