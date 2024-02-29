import { useCallback } from "react";
import styles from "./../../css/index/header.module.css";

const Header = () => {
  const onRectangleClick = useCallback(() => {
    // Please sync "/Sign-Up" to the project
  }, []);

  return (
    <section className={styles.header}>
      <div className={styles.header1} />
      <div className={styles.navbarFrame}>
        <div className={styles.fruitIcon}>
          <img className={styles.demo011Icon} alt="" src="/demo01-1@2x.png" />
          <img
            className={styles.iconVegetablesBroccoli}
            alt=""
            src="/icon--vegetables--broccoli@2x.png"
          />
          <img
            className={styles.arrowIcon0132}
            loading="lazy"
            alt=""
            src="/arrowicon01-3-2@2x.png"
          />
          <img
            className={styles.iconFruitsWatermelon}
            alt=""
            src="/icon--fruits--watermelon@2x.png"
          />
          <img
            className={styles.iconFoodFriedEggs}
            alt=""
            src="/icon--food--fried-eggs@2x.png"
          />
        </div>
        <div className={styles.textButton}>
          <div className={styles.eatSmarterGetFitterParent}>
            <div className={styles.eatSmarterGetContainer}>
              <p className={styles.eatSmarterGet}>EAT SMARTER. GET FITTER</p>
              <p className={styles.blankLine}>&nbsp;</p>
              <p className={styles.blankLine1}>&nbsp;</p>
              <p className={styles.blankLine2}>&nbsp;</p>
            </div>
            <h1 className={styles.tailoredNutritionForContainer}>
              <p className={styles.tailoredNutrition}>Tailored Nutrition,</p>
              <p className={styles.forYourUnique}>for Your Unique Lifestyle.</p>
              <p className={styles.blankLine3}>&nbsp;</p>
              <p className={styles.blankLine4}>&nbsp;</p>
              <p className={styles.blankLine5}>&nbsp;</p>
            </h1>
            <div className={styles.inputYourGoals}>
              Input your goals, and let's tailor your path to a healthier you
              with custom recipe plans.
            </div>
          </div>
          <div className={styles.rectangleParent}>
            <div className={styles.frameChild} onClick={onRectangleClick} />
            <b className={styles.tryForFree}>Try for free</b>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Header;
