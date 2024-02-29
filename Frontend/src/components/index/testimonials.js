import StarRatingSection from "./star-rating-section";
import styles from "./../../css/index/testimonials.module.css";

const Testimonials = () => {
  return (
    <section className={styles.testimonials}>
      <div className={styles.wrapperBg}>
        <img className={styles.bgIcon} alt="" src="/bg.svg" />
      </div>
      <div className={styles.logoffceWrapper}>
        <div className={styles.logoffce}>
          <StarRatingSection
            nutriPapiHasHelpedMeBalan="Nutri Papi has helped me balance my hectic life with my health goals. The recipes are quick, nutritious, and fit perfectly with my busy schedule. I feel healthier and more energized than ever before."
            paddyPimblett="Paddy Pimblett"
            fighter="Fighter"
            ellipseShape="/ellipse-1@2x.png"
          />
          <StarRatingSection
            nutriPapiHasHelpedMeBalan="Nutri Papi has completely transformed my approach to nutrition and wellness. The personalized meal plans not only helped me reach my target weight but also introduced me to a whole new world of flavors. It's like having a dietitian and a chef right at your fingertips!"
            paddyPimblett="Masa Kagami"
            fighter="McGill University Student"
            ellipseShape="/ellipse-1-1@2x.png"
            propLeft="-39px"
          />
          <StarRatingSection
            nutriPapiHasHelpedMeBalan="I was skeptical at first, but Nutri Papi proved me wrong. The ease of inputting my physical info and getting back a plan that actually fits my lifestyle and tastes is incredible. Plus, I've achieved my weight goals sooner than I expected. Highly recommend!"
            paddyPimblett="Wolfgang Amadeus Mozart"
            fighter="Musician"
            ellipseShape="/ellipse-1-2@2x.png"
            propLeft="-38px"
          />
        </div>
      </div>
      <h2 className={styles.testimonials1}>TESTIMONIALS</h2>
    </section>
  );
};

export default Testimonials;
